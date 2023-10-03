def randBG():
    fill(random())
    rect(0, 0, width(), height())
    fill(0)
    
for frame in range(20):
    frame += 1
    newPage()
    randBG()
    frameDuration(1/6)    
    font("Menlo")
    fontSize(300)
    text(str(frame), (width()/2, height()/2.3), align = "center")
    
saveImage("test.gif")