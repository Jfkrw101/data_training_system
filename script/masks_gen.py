import os
import cv2
from tqdm import tqdm
import argparse


# parser = argparse.ArgumentParser(description="Masks Gen")
# parser.add_argument("--data_name", type=str, required=True, help="Name Data folder you want for gen")
# args = parser.parse_args()


# cwd = os.getcwd()

# data_dir = cwd + '/data' + args.data_name
# images_dir = data_dir + '/images'
# maks_dir = data_dir + '/masks'

def masks_gen(images_path, mask_path):
    image_files = [f for f in os.listdir(images_path) if f.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tiff"))]

    os.makedirs(mask_path, exist_ok=True)

    for image_file in tqdm(image_files, desc="Processing Images"):
        input_path = os.path.join(images_path, image_file)
        output_path = os.path.join(mask_path, image_file)

        binary_mask = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        if binary_mask is None:
            print(f"Error: Failed to load the image '{input_path}'")
            continue

        binary_mask[binary_mask < 255] = 0
        cv2.imwrite(output_path, binary_mask)

        print(f"Modified mask image created successfully: '{output_path}'")
# masks_gen(images_dir,maks_dir)


