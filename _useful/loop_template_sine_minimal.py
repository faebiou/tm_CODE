fps = 30
seconds = 1
duration = 1 / fps
total = seconds * fps

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
    mover(frame) if frame <= total / 2 else mover(total - frame)
    
saveImage("looptest_minimal.gif")