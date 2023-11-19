#!/usr/bin/env python

from PIL import Image
import os

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as image:
        print(f"resizing: {input_path}")
        resized_image = image.resize(size)
        resized_image.save(output_path)

def resize_all_images(input_folder, output_folder, size):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            resize_image(input_path, output_path, size)

# Example usage
input_folder = "."
output_folder = "."
size = (800, 600)  # Specify the desired width and height

resize_all_images(input_folder, output_folder, size)
