# Hasty conversion utility for flame pendant project.  Takes a bunch of
# images (filenames received on command line) and outputs a big C array
# to use with the accompanying Arduino sketch.
# Typical invocation: python convert.py *.png > data.h
# Inputs are assumed valid; this does NOT perform extensive checking to
# confirm all images are the same size, etc.
# Requires Python and Python Imaging Library.

from PIL import Image
import sys

# --------------------------------------------------------------------------

cols     = 12 # Current column number in output (force indent on first one)
byteNum  = 0
numBytes = 0

def writeByte(n):
	global cols, byteNum, numBytes

	cols += 1                      # Increment column #
	if cols >= 12:                 # If max column exceeded...
		print                  # end current line
		sys.stdout.write("  ") # and start new one
		cols = 0               # Reset counter
	sys.stdout.write("{0:#0{1}X}".format(n, 4))
	byteNum += 1
	if byteNum < numBytes:
		sys.stdout.write(",")
		if cols < 11:
			sys.stdout.write(" ")

# --------------------------------------------------------------------------

prior    = None
bytes    = 0
numBytes = 0xFFFF

sys.stdout.write("const uint8_t PROGMEM anim[] = {")

for name in sys.argv[1:]: # For each image passed to script...
	image = Image.open(name)
	image.pixels = image.load()
	if image.mode != 'L': # Not grayscale? Convert it
		image = image.convert("L")
		image.pixels = image.load()
	# Gamma correction:
	for y in range(image.size[1]):
		for x in range(image.size[0]):
			image.pixels[x, y] = int(pow(
			  (image.pixels[x, y] / 255.0), 2.7) * 255.0 + 0.5)

	if prior:
		# Determine bounds of changed area
		x1 = image.size[0]
		y1 = image.size[1]
		x2 = y2 = -1
		for y in range(image.size[1]):
			for x in range(image.size[0]):
				if image.pixels[x, y] != prior.pixels[x, y]:
					if x < x1: x1 = x
					if x > x2: x2 = x
					if y < y1: y1 = y
					if y > y2: y2 = y
	else:
		# First image = full frame
		x1 = y1 = 0
		x2 = 8
		y2 = 15

	# Column major!
	writeByte((x1 << 4) | y1) # Top left corner
	writeByte((x2 << 4) | y2) # Bottom right corner
	bytes += 2
	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):
			writeByte(image.pixels[x, y])
			bytes += 1

	prior = image

writeByte(0xFF) # EOD marker
bytes += 1

print "};"
print
print "// " + str(bytes) + " bytes"
