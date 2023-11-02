import os
from PIL import Image

def convert_png_to_jpg_with_white_background(png_path, output_dir):
    # Open the PNG image
    png_image = Image.open(png_path)
    
    # Create a new image with a white background
    jpg_image = Image.new("RGB", png_image.size, (255, 255, 255))
    
    # Composite the PNG image onto the new JPEG image
    jpg_image.paste(png_image, mask=png_image.split()[3])
    
    # Save the JPEG image with white background
    jpg_filename = os.path.basename(png_path)[:-4] + ".jpg"  # Replace extension with .jpg
    jpg_path = os.path.join(output_dir, jpg_filename)
    jpg_image.save(jpg_path, "JPEG")

def convert_pngs_to_jpgs_with_white_background(png_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Iterate over all files in the directory
    for filename in os.listdir(png_directory):
        if filename.endswith(".png"):
            png_path = os.path.join(png_directory, filename)
            
            # Convert the PNG to JPEG with white background
            convert_png_to_jpg_with_white_background(png_path, output_directory)

# Provide the directory path containing the PNG files and the output directory path
name_data = 'cornflakes'
png_directory = f"/Users/jf/Desktop/drinks/{name_data}/images_png"
output_directory = f"/Users/jf/Desktop/drinks/{name_data}/images"

# Convert all PNGs to JPEGs with white background and save in the output directory
convert_pngs_to_jpgs_with_white_background(png_directory, output_directory)
