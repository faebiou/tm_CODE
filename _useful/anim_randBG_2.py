def randBG():
    fill(random(), random(), random())
    rect(0, 0, width(), height())
    fill(0, 0, 0)

frameNumber = 60
for frame in range(frameNumber):
    
    newPage(1080, 1920)
    frameDuration(1/60)
    fontSize(340)
    
    font("Skia")
    randBG()
    text("SUP", ((width()/2, height()/2)), align = "center")
    
    xpos = remap(frame, 0, frameNumber, 0, width())
    oval(xpos, 150, 100, 100)

for frame in range(frameNumber):
    
    newPage(1080, 1920)
    frameDuration(1/60)
    fontSize(340)
    
    font("Skia")
    randBG()
    text("SUP", ((width()/2, height()/2)), align = "center")
    
    xpos = remap(frame, frameNumber, 0, 0, width())
    oval(xpos, 150, 100, 100)

saveImage("test.gif")






