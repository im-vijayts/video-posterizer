from PIL import Image, ImageOps

image = Image.open('dp.jpg')

if image.mode == 'RGBA':
    image.load()
    r, g, b, a = image.split()
    image = Image.merge('RGB', (r, g, b))

im = ImageOps.posterize(image, 2)

im.show()