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
    s = 100
    fill(1, .6, 1)
    ratio = (width() - s)/ total * 2
    oval(step * ratio, 100, s, s)

for i in range(total):
    flip = True if i <= total / 2 else False
    looper(i, flip)

saveImage("looptest.gif", imageResolution = 10)

