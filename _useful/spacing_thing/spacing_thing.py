import os

count = 0

transX = 0
transY = 0

im = ImageObject()

size("A4Landscape")

s = 10
scale(1/s)
while transY < height()*s:
    transX = 0
    while transX < width()*s:
        path = randint(0, 6)
        im = "Hamburg/" + str(path) + ".png"
        x, y = imageSize(im)
        image(im, (transX, transY))
        transX += x
    transY += y