import os
import random
from PIL import Image, ImageFilter

TEST_DIR = "dataset/images/test"
TRAIN_DIR = "dataset/images/train"
TRAIN_LABELS = "dataset/labels/train"
TEST_LABELS = "dataset/labels/test"

def create_background():
    r, g, b = random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)
    background = Image.new('RGB', (640, 640), (r, g, b)).convert('RGBA')
    return background

def place_component(background, image, position):
    background.paste(image, position, image)
    return background

def maybe_blur(img, max_radius=3, probability=0.5):
    if random.random() < probability:
        radius = random.uniform(0, max_radius)
        img = img.filter(ImageFilter.GaussianBlur(radius=radius))
    return img

def augment_component(image, scale):   
    w, h = image.size
    image = image.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
    image = maybe_blur(image)
    return image

def check_overlap(box_placed, box_new):
    (min_x1, min_y1, max_x1, max_y1) = box_placed
    (min_x2, min_y2, max_x2, max_y2) = box_new
    return (min_x1 <= max_x2 and max_x1 >= min_x2 and
            min_y1 <= max_y2 and max_y1 >= min_y2)

def main():
    components = ["Voltage_Source", "Current_source", "Resistor", "Capacitor", "Inductor", "BJT", "MOSFET"]
    source_dir = "dataset/components"
    num_images = 1000
    train_split = 0.8
    train_images = int(train_split * num_images)

    # Overwrite check
    overwrite = input(f"[INFO] Overwriting existing dataset in dir dataset/images, (y/n) to continue..")
    if overwrite.lower() != 'y':
        print("[INFO] Exiting without overwriting dataset.")
        return

    # Make dirs
    os.makedirs(TRAIN_DIR, exist_ok=True)
    os.makedirs(TEST_DIR, exist_ok=True)
    os.makedirs(TRAIN_LABELS, exist_ok=True)
    os.makedirs(TEST_LABELS, exist_ok=True)

    for i in range(num_images):
        background = create_background()
        number_of_components = random.randint(1, 3)
        boxes = []
        labels = []

        for n in range(number_of_components):
            class_id = random.randint(0, len(components) - 1)
            component_type = components[class_id]
            component_dir = os.path.join(source_dir, component_type)
            image_file = random.choice(os.listdir(component_dir))
            image_path = os.path.join(component_dir, image_file)

            component = Image.open(image_path).convert("RGBA")

            overlap = True
            while overlap:
                scale = random.uniform(0.5, 1.5)
                augmented_component = augment_component(component, scale)

                position = (
                    random.randint(0, 640 - augmented_component.width),
                    random.randint(0, 640 - augmented_component.height)
                )

                min_x = position[0]
                max_x = position[0] + augmented_component.width
                min_y = position[1]
                max_y = position[1] + augmented_component.height

                new_box = (min_x, min_y, max_x, max_y)

                if n == 0:
                    overlap = False
                else:
                    overlap = any(check_overlap(b, new_box) for b in boxes)

            boxes.append(new_box)

            # Normalized YOLO coords
            x_centre = (position[0] + augmented_component.width / 2) / background.width
            y_centre = (position[1] + augmented_component.height / 2) / background.height
            w = augmented_component.width / background.width
            h = augmented_component.height / background.height

            labels.append(f"{class_id} {x_centre:.6f} {y_centre:.6f} {w:.6f} {h:.6f}")
            background = place_component(background, augmented_component, position)

        # Save image + labels
        image_name = f"image_{i}.png"
        label_name = f"image_{i}.txt"

        if i < train_images:
            save_path = os.path.join(TRAIN_DIR, image_name)
            label_path = os.path.join(TRAIN_LABELS, label_name)
        else:
            save_path = os.path.join(TEST_DIR, image_name)
            label_path = os.path.join(TEST_LABELS, label_name)

        background.save(save_path)
        with open(label_path, "w") as f:
            f.write("\n".join(labels))

if __name__ == "__main__":
    main()
