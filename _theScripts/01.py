# slightly more hardcore
# Ando's thing I guess
# object and label instead of variable

# newPage(1000, 1000)

def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)

def bullseye(steps):
    for i in range(steps):
        #        fill(i%2)
        fill(i % 2 * random())
        s = width() / steps
        midoval(width() / 2, height() / 2, width() - i * s)

def GifMe():
    for frames in range(10):
        newPage(1000, 1000)
        bullseye(20)
    saveImage("01.gif")
    

def fourOvals(x, y, r):
    midoval(x + r / 2, y + r / 2, r)
    midoval(x - r / 2, y + r / 2, r)
    midoval(x + r / 2, y - r / 2, r)
    midoval(x - r / 2, y - r / 2, r)

def ovals():
    r = 500
    for i in range(100):
        fill(i % 2,0,0)
        fourOvals(width() / 2, height() / 2, r)
        rotate(.1*i, (width() / 2, height() / 2))
        scale(0.98, center = (width()/2, height()/2))

ovals()

saveImage("_exp/01.pdf")
