for i in range(10):
    newPage(100*randint(1,3)/3, 30)
    fill(random())
    rect(0, 0, width(), height())

    fill(None)
    stroke(1,0,0)
    line((0, 0), (0, height()))
    stroke(0,0,1)
    line((width(), 0), (width(), height()))
    stroke(None)
    fill(0)
    font("Menlo")
    fontSize(12)
    text(str(i), (width()/2, 10), align = "center")
    saveImage(str(i) + ".png")