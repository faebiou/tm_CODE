import fun as f
import random

fg = ["#FFA6DD", "#FFF02A", "#6699FF", "#66FF95", "#FF4848"]
bg = ["#8200D4", "#001896", "#AA0045"]

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
    functions = [1, 2, 3, 4, 5]
    whichFunction = random.choice(functions)
    fill(*f.to_rgb(random.choice(fg)))

    if whichFunction == 1:
        rect(x, y, pixelSize, pixelSize)
    elif whichFunction == 2:
        oval(x, y, pixelSize, pixelSize)
    elif whichFunction == 3:
        triangle(x, y, pixelSize, pixelSize)
    elif whichFunction == 4:
        halfrect(x, y, pixelSize, pixelSize),
    elif whichFunction == 5:
        quart(x, y, pixelSize)
    
def drawPixelGlyph(pixelData):
    y = (ascender - 1) * pixelSize
    for row in pixelData.splitlines():
        x = 0
        for pixel in row:
            if pixel != " ":
                functionSelect(x, y, pixelSize)
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
            translate(0, -8* pixelSize)

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

def reshuffler(C):
    # s = randint(400, 800)
    s = 800
    x = width() * random.random()
    y = height() * random.random()
    drawPixelText(C, (x, y), s)
    
for frame in range(12):
    newPage(1080, 1920)
    frameDuration(1/2)
    
    fill(*f.to_rgb(random.choice(bg)))    
    rect(0, 0, width(), height())
    translate(0,-200)
    
    reshuffler("H")
    reshuffler("Y")
    reshuffler("P")
    reshuffler("E")
# for frame in range(4):
#     newPage(1080, 1920)
#     frameDuration(1/2)
    
#     fill(*f.to_rgb(random.choice(bg)))    
#     rect(0, 0, width(), height())
#     translate(0,-200)
#     drawPixelText("HYPE", (415, 1650), 400)
    
saveImage("_exp/" + f.fName() + ".gif")






