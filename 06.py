W = width()
H = height()

fill(None)

stroke(1,0,0)
lineCap("round")

# lineJoin("round") # radius = half of sw

for i in range(50):
    stroke(1 - pow(-1, i) , 0, 0)
    # stroke(i % 2, 0, 0)
    
    s = .5    
    lw = 230
    y = 762
    strokeWidth(1051-i*20)

    line((W/2,166),(W/2, y))
    line((W/2-lw, y),(W/2+lw, y))

    