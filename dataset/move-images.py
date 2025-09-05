import os
import argparse 
from imutils import paths
import shutil

BASEPATH = os.path.dirname(os.path.abspath(__file__))

#collects the file path to the csv files from the arg 
parser = argparse.ArgumentParser(description="csv file locations")
parser.add_argument("--file-dir", type=str, required=False, help="path to output directory")

args = parser.parse_args()

#joins the path to poin correctly
file_path = os.path.join(BASEPATH, args.file_dir)

for imagePath in paths.list_files(file_path, validExts=(".jpg", ".jpeg", ".png")):

    filename = os.path.basename(imagePath)

    destPath = os.path.join(BASEPATH, "circuits", "images", filename)

    shutil.move(imagePath, destPath)

print(f"[INFO] moved images to {file_path}")

if os.path.exists(file_path) and os.path.isdir(file_path):
    shutil.rmtree(file_path)
    print(f"[INFO] Deleted source directory: {file_path}")