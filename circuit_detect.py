import os
import cv2

def main():
    print("Welcome to Circuit Detect!")
    print("Created by Archie Eltherington")
    print("Version 1.0.0")
    input1 = ""
    while not os.path.exists("output"):
        input1 = input("[INFO] Please enter the path to the image file: ")

    img = cv2.imread(input1)