def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))


def messy(x, y, w, h):
    with savedState():
        translate(x + random(), y + random())
        rotate(random()*360)
        # scale(3)
        rect(0, 0, w, h)


def drawPixelGlyph(pixelData):
    y = (ascender - 1)  # initial value for y
    for row in pixelData.splitlines():
        x = 0  # initial value for x
        for pixel in row:
            # fill(0)
            l = .8
            if pixel == "x":
                fill(1-random()*l, 1-random()*l, 1-random()*l)
                rect(x, y, 1, 1)
            elif pixel == "o":
                fill(1-random()*l, 1-random()*l, 1-random()*l)
                oval(x, y, 1, 1)
            elif pixel == "i":
                fill(1-random()*l, 1-random()*l, 1-random()*l)
                rect(x, y, 1 / 2, 1)
            elif pixel == "v":
                fill(1-random()*l, 1-random()*l, 1-random()*l)
                triangle(x, y, 1, 1)
            elif pixel == "m":
                fill(1-random()*l, 1-random()*l, 1-random()*l)
                messy(x, y, 1, 1)
            x += 1
        y -= 1


def drawPixelText(txt, origin, fontSize):
    x, y = origin
    with savedState():
        translate(x, y)
        scale(fontSize/pixelsPerEm)
        for letter in txt:
            pixelData = pixelFont.get(letter, letter_notdef)
            drawPixelGlyph(pixelData)
            advance = len(letter_A)/len(letter_A.splitlines())
            translate(advance, 0)


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

letter_space = ""

pixelFont = {
    " ": letter_space,
    "A": letter_A,
    "B": letter_B,
    "C": letter_C,
    "D": letter_D,
    "R": letter_R
    }

ascender = 6
descender = -2

pixelsPerEm = ascender - descender

for frame in range(1):
    newPage(2000, 1000)
    blendMode("screen")

    fill(0)
    rect(0, 0, width(), height())

    translate(0,-20)
    for i in range(9):
        drawPixelText("ABRACADABRABRACADABRABRACADABRA", (-400+i*50, i*122), 134)
        
# saveImage("_exp/37.gif")