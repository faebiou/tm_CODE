size(2000, 1000)
def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))


def messy(x, y, w, h):
    with savedState():
        translate(x + randint(0, 50), y + randint(0, 50))
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)


def drawPixelGlyph(pixelData):
    y = (ascender - 1) * pixelSize  # initial value for y
    for row in pixelData.splitlines():
        x = 0  # initial value for x
        for pixel in row:
            # fill(0)
            if pixel == "x":
                rect(x, y, pixelSize, pixelSize)
            elif pixel == "o":
                oval(x, y, pixelSize, pixelSize)
            elif pixel == "i":
                rect(x, y, pixelSize / 2, pixelSize)
            elif pixel == "v":
                triangle(x, y, pixelSize, pixelSize)
            elif pixel == "m":
                messy(x, y, pixelSize, pixelSize)
            x = x + pixelSize
        y = y - pixelSize


def drawPixelText(txt, origin, fontSize):
    with savedState():
        scale(fontSize/unitsPerEm)
        for letter in txt:
            pixelData = pixelFont.get(letter, letter_notdef)
            drawPixelGlyph(pixelData)
            advance = len(letter_A)/len(letter_A.splitlines())
            translate(pixelSize * advance, 0)


letter_notdef = """\
xxxxx
x   x
x   x
x   x
x   x
xxxxx
"""

letter_A = """\
 xmx 
o   i
x   x
xxoxx
v   o
x   x
"""

letter_B = """\
xxxx 
x   x
xoxx
x   i
m   x
xxxx 
"""

letter_C = """\
 xxx 
x   x
o
x   
m   o
 xxx 
"""

letter_D = """\
oxxv 
x   o
i   x
x   i
x   x
xoxx 
"""

letter_R = """\
xxxx 
x   x
xoxx
x  m 
o   x
x   x
"""

pixelFont = {
    "A": letter_A,
    "B": letter_B,
    "C": letter_C,
    "D": letter_D,
    "R": letter_R
    }

ascender = 6
descender = -2

pixelsPerEm = ascender - descender

pixelSize = 100

unitsPerEm = pixelsPerEm * pixelSize

fill(0.2)
rect(0, 0, width(), height())
fill(0)

drawPixelText("ABRACADABRA", (100, 200), 300)