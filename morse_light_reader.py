# import the necessary packages
import numpy as np
import argparse
import cv2
import math
import re
from morse_converter import convertMorseToText
from time_estimator import *

def light_decoder(raw_light_sequence) -> list:
    # the longer light pulse is called dah
    dah = max(raw_light_sequence)

    decoded_morse = []
    for i in raw_light_sequence:
        if dah - 2 < i < dah + 2:
            decoded_morse.append('-')
        elif 0 < i < dah // 2:
            decoded_morse.append('.')
        else:
            decoded_morse.append(' ')
    return decoded_morse
    
def main():
    cap = cv2.VideoCapture(0)
    # adjust streaming params, more can be found here:
    # https://stackoverflow.com/questions/11420748/setting-camera-parameters-in-opencv-python

    cap.set(3,1280) # Width of the frames in the video stream
    cap.set(4,1024) # Height of the frames in the video stream
    cap.set(15, -8.0) # reduce exposure to limit noise light
    light_sequence = [0]
    pulse_instance = 0

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # apply blurring effect to reduce high frequency noise
        blurred = cv2.GaussianBlur(gray, (11, 11), 0)


        # apply threshold to convert images to binary
        thresh = cv2.threshold(blurred, 240, 255, cv2.THRESH_BINARY)[1]

        # apply erosions and dilations to reduce sparse spots
        thresh = cv2.erode(thresh, None, iterations=2)
        thresh = cv2.dilate(thresh, None, iterations=4)

        # find the curve of object's boundary
        cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        # create filter conditions for the object's shape and size
        min_area = 100
        total_light_area = 0

        for c in cnts:
            perimeter = cv2.arcLength(c, True)
            area = cv2.contourArea(c)
            circularity = 4*math.pi*(area/(perimeter*perimeter))

            if area > min_area and 0.6 < circularity < 1.2:
                cv2.drawContours(frame, [c], -1, (128,255,0), 2)
                total_light_area += area

        # log the light pulses as positive int and dark periods as 0s 
        if total_light_area > 0:
            light_sequence[-1] = light_sequence[-1] + 1
        else:
            light_sequence.append(0)

        # translate signal into text
        decoded = light_decoder(light_sequence)
        clean_morse = convertMorseToText(morse_cleaner(decoded))

        # annotate predicted texts on video stream
        cv2.putText(frame, "Message: " + clean_morse, (10, 470),
                        cv2.FONT_HERSHEY_DUPLEX, 0.7, (52, 152, 219), 2)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

if __name__ == '__main__':
    main()
    




