newPage(1080, 1920)
fontSize(340)

font("Menlo")

def randBG():
    fill(random(), random(), random())
    rect(0, 0, width(), height())
    fill(0)

randBG()
text("SUP", ((width()/2, height()/2.1)), align = "center")

saveImage("test.pdf")