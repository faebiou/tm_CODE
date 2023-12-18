def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))

def messy(x, y, w, h):
    with savedState():
        translate(x + w * random() / 2, y + h * random() / 2)
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)

def drawPixelGlyph(pixelData):
    y = (ascender - 1)  # initial value for y
    for row in pixelData.splitlines():
        x = 0  # initial value for x
        for pixel in row:
            # fill(0)
            if pixel == "x":
                rect(x, y, 1, 1)
            elif pixel == "o":
                oval(x, y, 1, 1)
            elif pixel == "i":
                rect(x, y, 1 / 2, 1)
            elif pixel == "v":
                triangle(x, y, 1, 1)
            elif pixel == "m":
                messy(x, y, 1, 1)
            # else:
            #     fill(0.9)
            #     oval(x, y, 1, 1)
            x = x + 1
        y = y - 1

def drawPixelText(txt, origin, fontSize):
    x, y = origin
    with savedState():
        translate(x, y)
        scale(fontSize / pixelsPerEm)
        for letter in txt:
            pixelData = pixelFont.get(letter, letter_notdef)
            drawPixelGlyph(pixelData)
            translate(6, 0)

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

letter_I = """\
 xxx
  x
  x
  x
  x
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
    "I": letter_I,
}

ascender = 6
descender = -2
pixelsPerEm = ascender - descender

# pixelSize = 1
unitsPerEm = pixelsPerEm
print(pixelsPerEm, unitsPerEm)

drawPixelText("ABBA", (58, 234), 216)
drawPixelText("ACAB", (102, 438), 216)
drawPixelText("BAIA", (102, 670), 216)

# # How to automate the drawing of multiple lines?
# txt = """ABBA
# ACAB
# BAAA"""

fill(1, 0, 0)
rect(0, 0, 100, 100)
