def randBG():
    # random fill 1
    fill(random(), random(), random())
    rect(0, 0, width(), height())
 
    # random fill 2
    fill(random(), random(), random())
    oval(10,10, 200,200)
 
    # reset to black
    fill(0, 0, 0)

# setting the fill to white won't matter because we are changing it in the function below
fill(1)

# executing the function we defined earlier
randBG()

# drawing the text
text("SUP", ((width()/2, height()/2)), align = "center")


for frame in range(10):
    newPage(1080, 1920)
    fontSize(340)
    font("Skia")
    
    randBG()
    text("SUP", ((width()/2, height()/2)), align = "center")



saveImage("test.gif")






