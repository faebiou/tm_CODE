W = width()
H = height()

fill(None)

stroke(1,0,0)
lineCap("round")
    
s = .5    
lw = 200
y = 752
b = 250
strokeWidth(100)
line((W/2,b),(W/2, y))
line((W/2-lw, y),(W/2+lw, y))

fill(None)
stroke(0)
lineCap("butt")
lineJoin("round")

strokeWidth(200)
lineDash(5,10,30,5,112,40,60,5,80)
rect(0, 0, W, H)