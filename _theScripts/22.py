letter_A = """\
 xxx  
x   x 
x   x 
xxxxx 
x   x 
x   x 
x   x 
"""

letter_C = """\
 xxx  
x   x 
x     
x     
x     
x   x 
 xxx  
"""

letter_O = """\
 xxx  
x   x 
x   x 
x   x 
x   x 
x   x 
 xxx  
"""

letter_T = """\
xxxxx 
  x   
  x   
  x   
  x   
  x   
 xxx  
"""


def pixelizer(letter, pixelSize):
    y = len(letter.splitlines())*100
    for row in letter.splitlines():
        x = 0
        for pixel in row:
            if pixel == "x":
                rect(x, y, pixelSize, pixelSize)
            else:
                oval(x + pixelSize / 4, y + pixelSize / 4, pixelSize/2, pixelSize/2)
            x += pixelSize
        y -= pixelSize
        

size = 11
offset = 6 * size

def tacoNOW():
    pixelizer(letter_T, size)
    translate(offset,0)
    pixelizer(letter_A, size)
    translate(offset,0)
    pixelizer(letter_C, size)
    translate(offset,0)
    pixelizer(letter_O, size)
    translate(-3*offset, 0)

for i in range(10):
    tacoNOW()
    translate(0, 100)
