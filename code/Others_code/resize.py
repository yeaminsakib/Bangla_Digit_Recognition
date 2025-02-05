import os
from PIL import Image

# Function to resize and compress images
def resize_and_compress_image(image_path, output_path, size=(244, 244), max_size_kb=10):
    img = Image.open(image_path)
    img = img.resize(size, Image.ANTIALIAS)  # Resize with antialiasing

    # Save the image with reduced quality to ensure it's under max_size_kb
    quality = 85  # Default quality
    img.save(output_path, optimize=True, quality=quality)

    # Check and resize image if size exceeds max_size_kb
    while os.path.getsize(output_path) > max_size_kb * 1024 and quality > 10:
        quality -= 5
        img.save(output_path, optimize=True, quality=quality)

# Function to process all images in a folder and its subfolders
def process_images(input_folder, output_folder, size=(244, 244), max_size_kb=10):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)
                
                output_dir = os.path.dirname(output_path)
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)

                resize_and_compress_image(file_path, output_path, size, max_size_kb)

# Define your input and output folders
input_folder = 'augmented_data'
output_folder = 'processed_data'

# Process the images
process_images(input_folder, output_folder)
