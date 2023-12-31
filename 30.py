test = """
..............
..............
..............
..............
..............
..............
....XXXXXX....
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
...XX....XX...
....XXXXXX....
..............
..............
..............
..............
..............
..............
..............
..............
"""

def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)


def midrect(x, y, r):
    rect(x - r / 2, y - r / 2, r, r)


def pixelizer(letter, pixelSize, whichFrame):
    y = 2000
    for row in letter.splitlines():
        x = 0
        for pixel in row:
            if pixel == "X":
                midoval(x, y, (halfFrames - whichFrame) * pixelSize / halfFrames * .8)
            elif pixel == ".":
                midoval(x, y, whichFrame * pixelSize / halfFrames * .8)
            x += pixelSize
        y -= pixelSize

pixel = 80
fRate = 30
halfFrames = 5

im = ImageObject()
blur = 3

for frame in range(halfFrames):
    newPage(1080, 1920)
    frameDuration(1/fRate)
    with im:
        fill(0.1)
        rect(0, 0, width(), height())
        fill(0, 0.9, 0.2)
        translate(pixel/4, 0)
        pixelizer(test, pixel, frame)

    image(im, (0, 0))
    im.gaussianBlur(blur)
    xoff, yoff = im.offset()
    image(im, (xoff, yoff))
    im.gaussianBlur(0)

    
for frame in range(halfFrames):
    newPage(1080, 1920)
    frameDuration(1/fRate)
    with im:
        fill(0.1)
        rect(0, 0, width(), height())
        fill(0, 0.9, 0.2)
        translate(pixel/4, 0)
        pixelizer(test, pixel, halfFrames-frame)

    image(im, (0, 0))
    im.gaussianBlur(blur)
    xoff, yoff = im.offset()
    image(im, (xoff, yoff))
    im.gaussianBlur(0)

saveImage("_exp/30.gif")
