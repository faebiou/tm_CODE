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
            # else:
            #     fill(0.9)
            #     oval(x, y, pixelSize, pixelSize)
            x = x + pixelSize
        y = y - pixelSize

def drawPixelText(txt, origin, fontSize):
    x, y = origin
    with savedState():
        translate(x, y)
        scale(fontSize / unitsPerEm)
        for letter in txt:
            pixelData = pixelFont.get(letter, letter_notdef)
            drawPixelGlyph(pixelData)
            translate(6 * pixelSize, 0)

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
x   x
xxxx
"""

letter_C = """\
 xxx
x   x
o
x
x   o
 xxx
"""

letter_space = ""

letter_notdef = """\
xxxxx
x   x
x   x
x   x
x   x
xxxxx
"""

pixelFont = {
    " ": letter_space,
    "A": letter_A,
    "B": letter_B,
    "C": letter_C,
}
ascender = 6
descender = -2
pixelsPerEm = ascender - descender

pixelSize = 100
unitsPerEm = pixelsPerEm * pixelSize
print(pixelsPerEm, unitsPerEm)

# drawPixelGlyph(letter_A)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_B)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_B)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_A)

drawPixelText("ABBA", (102, 200), 216)
drawPixelText("ACAB", (102, 438), 216)
drawPixelText("BAAA", (102, 670), 216)

fill(1, 0, 0)
rect(0, 0, 100, 100)
