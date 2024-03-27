def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))

def messy(x, y, w, h):
    with savedState():
        translate(x + randint(0, w), y + randint(0, h))
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)

def quart(xo, yo, r):
    with savedState():
        rotate(0, center=(xo + r/2, yo + r/2))        
        p = BezierPath()
        p.moveTo((xo + r, yo))
        p.lineTo((xo, yo))
        p.lineTo((xo, yo + r))
        p.arcTo((xo + r, yo + r), (xo + r, yo), r)
        drawPath(p)

def halfrect(x, y, r, p):
    rect(x,y, r/2, p)

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
                halfrect(x, y, pixelSize, pixelSize),
            elif pixel == "v":
                triangle(x, y, pixelSize, pixelSize)
            elif pixel == "m":
                # messy(x, y, pixelSize, pixelSize)
                quart(x, y, pixelSize)
            x = x + pixelSize
        y = y - pixelSize

def drawPixelText(txt, origin, fontSize):
    x, y = origin
    with savedState():
        translate(x, y)
        scale(fontSize / unitsPerEm)
        for letter in txt:
            pixelData = pixelFont.get(letter)
            drawPixelGlyph(pixelData)
            translate(6 * pixelSize, 0)

letter_T = """\
vxiao 
x x x
  o   
  v  
  a  
 aiv
"""
    
letter_H = """\
x   i
a   i
axoix
x   a
v   o
x   x
"""

letter_Y = """\
x   i 
o   x
 imi
  v 
  a  
 moa
"""

letter_P = """\
xmiiv
x   x
a   i
xoao 
v    
o    
"""

letter_E = """\
xxmo 
x    
a    
xom    
i    
xxox
"""

pixelFont = {
    "T": letter_T,    
    "H": letter_H,
    "Y": letter_Y,
    "P": letter_P,
    "E": letter_E,
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

drawPixelText("HYPE", (100, 800), 200)
drawPixelText("TYPE", (100, 610), 200)