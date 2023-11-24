def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))

def messy(x, y, w, h):
    with savedState():
        translate(x + randint(0, w), y + randint(0, h))
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)
        
# def quarter should be here in some way?
def quart(xo, yo, r):
    with savedState():
        rotate(0, center=(xo + r/2, yo + r/2))        
        p = BezierPath()
        p.moveTo((xo + r, yo))
        p.lineTo((xo, yo))
        p.lineTo((xo, yo + r))
        p.arcTo((xo + r, yo + r), (xo + r, yo), r)
        drawPath(p)

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
            elif pixel == "a":
                triangle(x, y, pixelSize, pixelSize)
            elif pixel == "i":
                rect(x, y, pixelSize / 2, pixelSize),
                line((x, pixelSize), (pixelSize, y))
            elif pixel == "v":
                triangle(x, y, pixelSize, pixelSize)
            elif pixel == "m":
                # messy(x, y, pixelSize, pixelSize)
                quart(x, y, pixelSize)
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
a   i
a   x
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
 xmiv
x   x
x  
x   
x   x
 xox
"""

letter_D = """\
xxmo 
x   x
x   i
x   i
x   x
xxxx
"""

letter_F = """\
xxmox
x
x
xxxi
x 
x
"""

letter_U = """\
x   x
o   i
x   x
x   x
x   o
 xov 
"""

letter_K = """\
x  m
x x
mx
x v
x  v
x   x
"""

letter_exclam = """\
 mi
 xi
 x
 i
  
 o
"""

letter_space = ""

letter_notdef = """\

xxxxx
x x x
xxxxx
x x x
xxxxx
"""


pixelFont = {
    " ": letter_space,
    "!": letter_exclam,
    "A": letter_A, 
    "B": letter_B,
    "C": letter_C,
    "D": letter_D,
    "F": letter_F,
    "U": letter_U,
    "K": letter_K,

}

ascender = 6
descender = -2
pixelsPerEm = ascender - descender # --> 8

pixelSize = 10
unitsPerEm = pixelsPerEm * pixelSize


# drawPixelGlyph(letter_A)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_C)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_B)
# translate(6 * pixelSize, 0)
# drawPixelGlyph(letter_D)

drawPixelText("IRSTJ", (100, 800), 200)
drawPixelText("AB DA", (100, 600), 200)
drawPixelText("DABBA", (100, 400), 200)
drawPixelText("FUCK!", (100, 200), 200)
drawPixelText("IRSTJ", (100, 25), 200)

#you want to automate the lines above with line height.
# txt = """ABBA
# ACAB
# BAAA"""




fill (1,0,0)
rect (0, 0, 100, 100)


