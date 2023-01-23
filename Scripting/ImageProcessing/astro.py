from PIL import Image

img = Image.open("./astro.jpg")
# resized = img.resize((400, 400))
img.thumbnail((400, 400))
print(img.size)  # 400x381
img.save("resize.jpg")
