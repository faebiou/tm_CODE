import fun as f

framesPerSecond = 30
numFrames = 60

canvasWidth = 600
canvasHeight = 600

for frame in range(numFrames):
    t = frame / numFrames

    # tt = (-cos(2 * pi * t) + 1) / 2
    tt = (sin(2 * pi * t - pi/2) + 1) / 2

    newPage(canvasWidth, canvasHeight)
    frameDuration(1 / framesPerSecond)
    fill(tt, 0, 1 - tt)
    rect(0, 0, width(), height())

    x = 400 * tt

    fill(1)
    rect(x, 100, 200, 200)

saveImage("_exp/44.gif")
