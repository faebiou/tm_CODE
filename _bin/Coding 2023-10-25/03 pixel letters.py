def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))

def messy(x, y, w, h):
    with savedState():
        translate(x + randint(0, 50), y + randint(0, 50))
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)

def drawPixelGlyph(pixelData):
    y = 784  # initial value for y
    for row in pixelData.splitlines():
        x = 60  # initial value for x
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

def drawPixelText(txt):
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

letter_notdef = """\
xxxxx
x   x
x   x
x   x
x   x
xxxxx
"""

pixelFont = {
    "A": letter_A,
    "B": letter_B,
    "C": letter_C,
}

pixelSize = 100


scale(0.3)

# drawPixelGlyph(letter_A)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_B)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_B)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_A)

drawPixelText("ABBACAD")
