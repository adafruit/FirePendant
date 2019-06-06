# This repository has been archived

The contents were mirrored to https://github.com/adafruit/Adafruit_Learning_System_Guides/tree/master/Trinket_Pro_Fire_Pendant

The files in this repository accompanied an [Adafruit Learning System](https://learn.adafruit.com) tutorial 
https://learn.adafruit.com/animated-flame-pendant

## FirePendant

Fire pendant jewelry for Adafruit Pro Trinket + Charlieplex LED array. Loops a canned animation sequence on the display.

Arduino sketch is comprised of 'FirePendant.ino' and 'data.h' -- latter contains animation frames packed into PROGMEM array holding bounding rectangle + column-major pixel data for each frame (consumes most of the flash space on the ATmega328).

The 'frames.zip' archive contains the animation source PNG images and a python script, convert.py, which processes all the source images into the required data.h  format. The PNG images were generated via Adobe Premiere and Photoshop from Free Stock Video by user 'dietolog' on Videezy.com.

Please consider buying your parts at [Adafruit.com](https://www.adafruit.com) to support open source code.
