translate(500, 500)

with savedState():
    rotate(20) 
    for i in range(100):
        stroke(0)
        rect(200, 0, 98, 10)
        rotate(32 + random())
        scale(.99)
        stroke(None)

fill(1, 0, 0, .8)
squareSize = 214

translate(-squareSize/2, -squareSize/2)
rect(0, 0, squareSize, squareSize)