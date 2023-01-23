"""
Program to convert .jpg images to .png format.
"""

import sys
import os
from PIL import Image

# Grab arguments
in_dir, out_dir = sys.argv[1], sys.argv[2]

# Check output path
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

# Convert images
for idx, img_path in enumerate(os.listdir(in_dir)):
    try:
        path = os.path.join(in_dir, img_path)
        img = Image.open(path)
        img.save(os.path.join(out_dir, os.path.splitext(img_path)[0] + ".png"))
        print(f"Image {idx} done!")
    except FileNotFoundError as e:
        print("Image file not found!")
    except IOError as e:
        print("Could not read the image!")
