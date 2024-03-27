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


def quart(x, y, t):
    if t == 1:
        fill(0.8)
        midrect(0, 0, pixelSize)
    elif t == 2:
        fill(0.6)
        midrect(x, pixelSize* ratio, pixelSize)
        midrect(pixelSize* ratio, pixelSize* ratio, pixelSize)
        midrect(pixelSize* ratio, y, pixelSize)

    elif t == 3:
        fill(0.4)
        midrect(x, 2 * pixelSize* ratio, pixelSize)
        midrect(x, 2 * pixelSize* ratio, pixelSize)
        midrect(pixelSize* ratio, 2 * pixelSize* ratio, pixelSize)
        midrect(2 * pixelSize* ratio, pixelSize* ratio, pixelSize)
        midrect(2 * pixelSize* ratio, y, pixelSize)

    elif t == 4:
        fill(0.2)
        midrect(x, 3 * pixelSize* ratio, pixelSize)
        midrect(2 * pixelSize* ratio, 2 * pixelSize* ratio, pixelSize)
        midrect(x, 3 * pixelSize* ratio, pixelSize)
        midrect(pixelSize* ratio, 3 * pixelSize* ratio, pixelSize)
        midrect(3 * pixelSize* ratio, pixelSize* ratio, pixelSize)
        midrect(3 * pixelSize* ratio, y, pixelSize)


def explode(x, y, t):
    for deg in range(4):
        rotate(deg * 90)
        quart(x, y, t)


def pixelizer(letter, pixelSize, whichFrame):
    y = 2000
    for row in letter.splitlines():
        x = 0
        for pixel in row:
            if pixel == "X":
                explode(x, y, whichFrame%4)
            elif pixel == ".":
                explode(x, y, 1-whichFrame%4)
            x += pixelSize
        y -= pixelSize


pixelSize= 20
ratio = 1.5

pixel = 80
fRate = 10
halfFrames = 4

for frame in range(halfFrames):
    newPage(1080, 1920)
    frameDuration(1 / fRate)
    fill(0.1)
    rect(0, 0, width(), height())
    fill(0, 0.9, 0.2)
    translate(pixel / 4, 0)
    pixelizer(test, pixel, frame)

# for frame in range(halfFrames):
#     newPage(1080, 1920)
#     frameDuration(1 / fRate)
#     fill(0.1)
#     rect(0, 0, width(), height())
#     fill(0, 0.9, 0.2)
#     translate(pixel / 4, 0)
#     pixelizer(test, pixel, halfFrames - frame)

saveImage("_exp/31.gif")
