import torch 
import os

BASE_PATH = 'dataset'
IMAGES_DIR = os.path.sep.join([BASE_PATH, "images"])
CSV_DIR= os.path.sep.join([BASE_PATH, "annotations"])

MODEL_WEIGHTS = "/opt/homebrew/runs/detect/train14/weights/best.pt"

# determine the current device and based on that set the pin memory
DEVICE = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

IMG_SIZE = 640
NUM_EPOCHS = 50
BATCH_SIZE = 16
