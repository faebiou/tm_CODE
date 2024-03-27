box = (120, 120, 540, 740)
x, y, w, h = box
inset = 23

smallerBox = (x + inset, y + inset, w - inset * 2, h - inset * 2)

fill(.5)
rect(*box)

fill(.1)
rect(*smallerBox)