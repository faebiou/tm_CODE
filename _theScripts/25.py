# pixel font drawing or something

translate(500, 500)
scale(.5)

def pix():

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
    fill(0)
    
W_step = int(width()/10)
H_step = int(height()/10)

for i in range(0, width(), W_step):
    with savedState():
        translate(W_step, 0)
        for i in range(0, width(), H_step):
            with savedState():
                translate(0, H_step)
                pix()