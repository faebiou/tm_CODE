# homework
# add explanation?

newPage(1000, 1000)

baseline = 250
capheight = 520

strokeW = 80

letterwidth = 389

ratio = 0.5

rect(width()/2 - strokeW/2, baseline, strokeW, capheight)
rect(width()/2 - letterwidth/2, baseline + capheight - strokeW*ratio, letterwidth, strokeW*ratio)