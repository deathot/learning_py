from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# im = Image.open('taobi.jpg')
# w, h = im.size
# print('Original image size: %sx %s' % (w, h))

# im.thumbnail((w//32, h//32))
# print('Resize image to: %sx %s' % (w//32, h//32))

# im.save('thumbnail0.jpg', 'jpeg')

# im = Image.open('thumbnail0.jpg')
# im1 = im.filter(ImageFilter.BLUR)
# im1.save('blur.jpg', 'jpeg')

#random Char
def rndChar():
    return chr(random.randint(65, 90))

#random color0
def rndColor0():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#random color1
def rndColor1():
    return (random.randint(32, 127))

#240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

#font instance songti 36
font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 36)

#draw instance
draw = ImageDraw.Draw(image)

#填充像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill = rndColor0())

#out word
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font = font, fill = rndColor1())

#BLUR
image = image.filter(ImageFilter.BLUR)
image.save('BLur_random1.jpg', 'jpeg')
