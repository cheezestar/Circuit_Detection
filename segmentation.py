from ultralytics import YOLO
import setup.config as CONFIFG

def train_yolo(path):
    # Load a pretrained YOLOv8 model
    model = YOLO("yolo11s-seg")
    model.train(
        data=path,  
        epochs= CONFIFG.NUM_EPOCHS,                  
        imgsz=CONFIFG.IMG_SIZE,                    
        batch=CONFIFG.BATCH_SIZE,                 
    )
    
    metrics = model.val()  
    print(metrics)        
 
def main():
    command = input("Enter datset path")
    train_yolo(command)