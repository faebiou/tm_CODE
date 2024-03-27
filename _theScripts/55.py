import fun as f

def triangle(x, y, w, h):
    polygon((x, y), (x, y + h), (x + w, y))

def messy(x, y, w, h):
    with savedState():
        translate(x + randint(0, w), y + randint(0, h))
        rotate(10)
        # scale(3)
        rect(0, 0, w, h)

def quart(x, y, r):
    with savedState():
        rotate(0, center=(x + r/2, y + r/2))        
        p = BezierPath()
        p.moveTo((x + r, y))
        p.lineTo((x, y))
        p.lineTo((x, y + r))
        p.arcTo((x + r, y + r), (x + r, y), r)
        drawPath(p)

def halfrect(x, y, r, p):
    rect(x,y, r/2, p)
    

def functionSelect(x, y, r):
    rect
    oval
    triangle
    halfrect    

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
xxxxx 
x x x
  x   
  x  
  x  
 xxx
"""
    
letter_H = """\
x   x
x   x
xxxxx
x   x
x   x
x   x
"""

letter_Y = """\
x   x 
x   x
 xxx
  x 
  x  
 xxx
"""

letter_P = """\
xxxxx
x   x
x   x
xxxx 
x    
x    
"""

letter_E = """\
xxxx 
x    
x    
xxx    
x    
xxxx
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


for frame in range(4):
    newPage(1080, 1920)
    frameDuration(1/2)
    translate(0,-150)
    for i in range(10):
        drawPixelText("TYPE", (120, i * 300 + frame * 75), 300)

for frame in range(4):
    newPage(1080, 1920)
    frameDuration(1/2)
    translate(0,-150)
    for i in range(10):
        drawPixelText("HYPE", (120, i * 300 + frame * 75), 300)
    
saveImage("_exp/" + f.fName() + ".gif")






