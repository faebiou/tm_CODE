# homework alt

baseline = 0
capheight = 200

strokeW = 30

letterwidth = 180

ratio = 0.7

def tFill(t):
    fill(random()*t,random()*t, random()*t)

def T():
    tFill(.9)
    rect(width()/2 - strokeW/2, baseline, strokeW, capheight)
    rect(width()/2 - letterwidth/2, baseline + capheight - strokeW*ratio, letterwidth, strokeW*ratio)
    
def Ts(n):
    tFill(.3)
    rect(0, 0, width(), height())
    for i in range(n):
        with savedState():
            translate((2*random()-1)*width(), (2*random()-1)*height())
            rotate(random()*180, (width()/2, height()/2))
            T()

for frames in range(12):
    newPage(1000, 1000)
    frameDuration(1/2)         
    Ts(200)

# saveImage("_exp/03.gif")