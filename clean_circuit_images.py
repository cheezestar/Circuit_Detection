import os
import cv2
import numpy as np
import setup.config as CONFIFG
import matplotlib.pyplot as plt
from ultralytics import YOLO

img_num = 0 
#workflow removes components using my trained component detection model
#then cleans background to leave wires only
#this is a key part of the workflow in order to be able to train a wire tracing model 
#this will allow me eventually to use logic to build a circuit netlist


def clean_image(model, image_path):
    results = model(image_path)
    bboxes = []

    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = box.xyxy[0].tolist()   # pixel coords
            conf = float(box.conf[0])               # confidence
            cls = int(box.cls[0])                   # class 
            bboxes.append((x1, y1, x2, y2, conf, cls))
            print(f"Class {cls} | Conf {conf:.2f} | BBox: ({x1}, {y1}, {x2}, {y2})")


    if len(bboxes) <= 1:
        return
    
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # grayscale image
    thresh = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV,
        blockSize=15, 
        C=10           
    )

    kernel = np.ones((2, 2), np.uint8)
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    dilated = cv2.dilate(clean, kernel, iterations=1)

    # remove components
    for box in bboxes:
        x1, y1, x2, y2, conf, cls = map(int, box[:6])
        dilated[y1:y2, x1:x2] = 0   
    
    # save cleaned image
    fileName = f"cleaned_circuit_{img_num}.png"
    savePath = os.path.join("dataset/wires", fileName)
    cv2.imwrite(savePath, dilated)
    img_num += 1

def main():
    model = YOLO(CONFIFG.MODEL_WEIGHTS)
    dir = "dataset/raw/train/images"
    for imgs in os.listdir(dir):
        if imgs.endswith((".jpg", ".jpeg", ".png")):
            print(f"Processing image: {imgs}")
            img_path = os.path.join(dir, imgs)
            clean_image(model, img_path)

if __name__ == "__main__":
    main()