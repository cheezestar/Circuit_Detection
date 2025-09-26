import setup.config as CONFIFG
import cv2
from ultralytics import YOLO

model = YOLO(CONFIFG.MODEL_WEIGHTS)
path = input("Please enter image path:  ")
results = model(path)

# Print bounding box results
for result in results:
    for box in result.boxes:
        x1, y1, x2, y2 = box.xyxy[0].tolist()   # absolute pixel coords
        conf = float(box.conf[0])               # confidence
        cls = int(box.cls[0])                   # class id
        print(f"Class {cls} | Conf {conf:.2f} | BBox: ({x1}, {y1}, {x2}, {y2})")

# Loop through results and display with OpenCV
for result in results:
    img = result.plot()   # this draws boxes, labels, confidences on the image
    cv2.imshow("YOLOv8 Prediction", img)

    # wait until key press (0 = forever, or give ms for auto-close)
    cv2.waitKey(0)

cv2.destroyAllWindows()