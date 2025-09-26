import os
import shutil
import setup.config as CONFIFG

BASEPATH = 'dataset'

def clear_dataset():
    if os.path.exists(BASEPATH):
        shutil.rmtree(BASEPATH)
    os.makedirs(os.path.sep.join([BASEPATH, "images"]))
    os.makedirs(os.path.sep.join([BASEPATH, "annotations"]))


def main():
    command = input("Enter command")
    if command == "clear":
        clear_dataset()
        print("Dataset cleared")
    elif command == "":
        print("No command entered")
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()