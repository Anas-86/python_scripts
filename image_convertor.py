import os
import sys
import pathlib
from PIL import Image
from pathlib import Path


# grab first and second argument. first argument file to read, second file to write
# check if out path exists or not. if not create it.
def process_paths(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        print(f"Input path '{input_path}' is invalid.")
        return False

    if not output_path.exists():
        print(f"Output path '{output_path}' does not exist. Setting to default output path.")
        return False
    return True  # Both paths are valid


# loop through mpeg photos in file to read
def convert_images_to_png(input_path, output_path):
    input_path = Path(input_path)
    output_path = Path(output_path)
    for image_file in input_path.glob('*'):
        img = Image.open(image_file)
        output_file = output_path / (image_file.stem + '.png')
        img.save(output_file, 'PNG')
        print(f"Converted '{image_file}' to '{output_file}'")


# convert images to png.

def start_converting(input_path, output_path):
    if process_paths(input_path, output_path):
        convert_images_to_png(input_path, output_path)
    else:
        folder_to_create = 'C:\\Users\\anask\\Desktop\\outputFolder'
        # Create the folder
        os.makedirs(folder_to_create, exist_ok=True)
        output_path = Path(folder_to_create)
        convert_images_to_png(input_path, output_path)


"""
The method start_converting
is going to convert the images in a given path to the format of png
you can adapt the code accordingly to convert images to a special image type.
the default heir is * which corresponds to all types
and the output is set to png by default.
"""
start_converting('C:\\Users\\anask\\Desktop\\pokemonPhotos', 'C:\\Users\\anask\\Desktop\\pokemonPhotosConverted')
