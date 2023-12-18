fps = 30
seconds = 3
duration = 1 / fps
total = seconds * fps

def looper(value, flipped):
    mover(value) if flipped else mover(total - value)

def mover(step):
    newPage()
    fill(1)
    rect(0, 0, width(), height())
    frameDuration(duration)
    t = step / total
    tt = (sin(2 * pi * t - pi/2) + 1) / 2
    
    ballSize = 200
    fill(0)    
    x = (width() - ballSize) * tt
    oval(x, height()/2 - ballSize/2, ballSize, ballSize)

for frame in range(total):
    flip = True if frame <= total / 2 else False
    looper(frame, flip)

saveImage("looptest.gif")