# taco = """\
# xxxxxx 
#   x  xxxx   xxx   xxx
#   x   x x  x     x   x
#   x  x   x  xxx   xxx
  
# """ * 8

letter_A = """\
 xxx   x   x   xxx   x
x   x  x   x  x   x  x
x   x  x   x  x   x  x
xxxxx  xxxxx  xxxxx  x
x   x  x   x  x   x  x
x   x  x   x  x   x   
x   x  x   x  x   x  x
"""


pixelSize = 45
y = len(letter_A.splitlines())*100

# turn this into a function

for row in letter_A.splitlines():
    x = 0
    for pixel in row:
        if pixel == "x":
            rect(x, y, pixelSize, pixelSize)
        else:
            oval(x+pixelSize/4, y+pixelSize/4, pixelSize/2, pixelSize/2)
        x += pixelSize
    y -= pixelSize
