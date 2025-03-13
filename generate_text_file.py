import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def save_sequential_image_names(directory, output_file):
    image_extensions = ('.png', '.jpg', '.jpeg')
    image_files = [f for f in os.listdir(directory) if f.lower().endswith(image_extensions)]
    
    image_files.sort(key=natural_sort_key)
    with open(output_file, 'w') as file:
        for image in image_files:
            filename = os.path.splitext(image)[0]
            file.write(f"{filename}\n")
    
    print(f"Saved {len(image_files)} image filenames (without extensions) to {output_file} in sequential order.")

directory = 'frames'
output_file = 'panama_image_sequence.txt'

save_sequential_image_names(directory, output_file)
