def D(x1, y1, x2, y2):
    return(sqrt())
def midoval(x, y, r):
    oval(x - r/2, y - r/2, r, r)

def midrect(x, y, r):
    rect(x - r/2, y - r/2, r, r)

def triangle(x, y, h):
    a = (2 / sqrt(3))*h
    polygon((x - a/2, y - h/2), (x, y + h/2), (x + a/2, y - h/2))            
            
A_left = """\
. 
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
x
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
"""

blank = """\
 
 
 
 
 
 
 
"""

def pixelizer(letter, pixelSize):
    y = H/1.25
    for row in letter.splitlines():
        x = 0
        for pixel in row:
            if pixel == "x":
                midoval(x, y, pixelSize*.8)
            elif pixel == ".":
                triangle(x, y, pixelSize*.5)
            else:
                midrect(x, y, pixelSize*.5)
            x += pixelSize
        y -= pixelSize

newPage()

W = width()
H = height()

pix = 107
stroke(1,0,0)
line((W/2, 0), (W/2, H))
stroke(None)

var = 5
translate(width() / 2, 0)
for v in range(int(var-var/3)):
    translate(-pix, 0)
pixelizer(A_left, pix)
translate(pix, 0)
for i in range(var):
    pixelizer(A_mid, pix)
    translate(pix, 0)
pixelizer(A_right, pix)
