# Morse-Light-Translator-OpenCV
 A program that decrypts Morse Code from a light source (LED Flash, bulb, etc.) using OpenCV.

## What is Morse Code?
Morse code is a method of transmitting text information as a series of on-off tones, lights, or clicks that can be directly understood by a skilled listener or observer without special equipment. It is named for Samuel F. B. Morse, an inventor of the telegraph.

## How it works?

This project translates morse code from blinking light into plain English. A webcam is used to read the pulsing of a smartphone's flashlight, which then can be converted to Latin alphabet, including numbers and some punctuations. 

The decoding is done in real-time.

![gif](/static/cap.gif)

## How to run?


Install the requirements.txt and run the main module: `morse_light_reader.py`. Ctrl + C to escape video stream.
