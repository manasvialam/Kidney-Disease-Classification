import os
import shutil

# Define source and destination directories
source_dir = '/Users/manasvialam/Downloads/archive/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone/CT-KIDNEY-DATASET-Normal-Cyst-Tumor-Stone'  # Replace with your source folder path
destination_dir = '/Users/manasvialam/Documents/ML_projects/Kidney_imagedata'  # Replace with your destination folder path

# Ensure destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# List all files in the source directory and filter out image files
image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')
images = [f for f in os.listdir(source_dir) if f.lower().endswith(image_extensions)]

# Sort and take the first 300 images
first_300_images = images[:300]

# Transfer the first 300 images
for image in first_300_images:
    source_path = os.path.join(source_dir, image)
    destination_path = os.path.join(destination_dir, image)
    
    # Move the image from source to destination
    shutil.move(source_path, destination_path)

print(f"Transferred {len(first_300_images)} images from {source_dir} to {destination_dir}.")
