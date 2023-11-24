def D(x1, y1, x2, y2):
    return sqrt()


def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)


def midrect(x, y, r):
    rect(x - r / 2, y - r / 2, r, r)


def triangle(x, y, h):
    r = random() * 360
    with savedState():
        rotate(r, center=(x, y))
        a = (2 / sqrt(3)) * h
        polygon((x - a / 2, y - h / 2), (x, y + h / 2), (x + a / 2, y - h / 2))
    # a = (2 / sqrt(3)) * h
    # polygon((x - a / 2, y - h / 2), (x, y + h / 2), (x + a / 2, y - h / 2))


A_left = """\
.
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
"""

A_mid = """\
x
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
x
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
"""

A_right = """\
.
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
x
"""

blank = """"""


def pixelizer(letter, pixelSize):
    y = height() / 2
    for row in letter.splitlines():
        x = 0
        for pixel in row:
            if pixel == "x":
                midoval(x, y, pixelSize * 0.7)
            elif pixel == ".":
                triangle(x, y, pixelSize * 0.5)
            else:
                midrect(x, y, pixelSize * 0.5)
            x += pixelSize
        y -= pixelSize


def loop():
    frameControl = 15
    posControl = 850

    for frame in range(frameControl):

        newPage(1080, 1920)
        fill(0.1)
        rect(0, 0, width(), height())
        fill(0, 0.9, 0.3)

        W = width()
        H = height()

        pix = 50

        var = frame + 2
        translate(100, posControl)
        pixelizer(A_left, pix)
        for i in range(0, var, 1):
            translate(pix, 0)
            pixelizer(A_mid, pix)
        translate(pix, 0)
        pixelizer(A_right, pix)

    for frame in range(frameControl):

        newPage(1080, 1920)
        fill(0.1)
        rect(0, 0, width(), height())
        fill(0, 0.9, 0.3)

        W = width()
        H = height()

        pix = 50

        var = frameControl - frame + 2
        translate(950, posControl)
        pixelizer(A_left, pix)
        for i in range(var - 1, 0, -1):
            translate(-pix, 0)
            pixelizer(A_mid, pix)
        translate(-pix, 0)
        pixelizer(A_right, pix)

    for frame in range(frameControl):

        newPage(1080, 1920)
        fill(0.1)
        rect(0, 0, width(), height())
        fill(0, 0.9, 0.3)

        W = width()
        H = height()

        pix = 50
        var = frameControl - frame + 4
        translate(var * pix, posControl)
        pixelizer(A_left, pix)
        translate(-pix, 0)
        pixelizer(A_mid, pix)
        translate(-pix, 0)
        pixelizer(A_mid, pix)
        translate(-pix, 0)
        pixelizer(A_right, pix)


for loops in range(1):
    loop()

saveImage("_exp/26.gif")
