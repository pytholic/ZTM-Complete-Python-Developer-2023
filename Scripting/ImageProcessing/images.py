import numpy as np
from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")

# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))


# filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert("L")
# rotate = filtered_img.rotate(90)
# resize = filtered_img.resize((300, 300))
box = (100, 100, 400, 400)
crop = filtered_img.crop(box)

# filtered_img = filtered_img.convert("RGB")  # back to 3 channed for np cpncat

# We save image
# filtered_img.save("blur.png", "png")

# Show result
# filtered_img.show()
# rotate.show()
# resize.show()
crop.show()

# Show side-by-side
# img = np.asarray(img)
# filtered_img = np.asarray(filtered_img)
# concatenate = np.concatenate((img, filtered_img), axis=1)

# result = Image.fromarray(np.uint8(concatenate))
# result.show()
