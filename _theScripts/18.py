path = "/Users/faebiou/Documents/TM_2324/_MISC/STUFF/mutatorSans-master/MutatorSans-VF.ttf"


for frame in range(48):
    newPage(1080, 1920)
    frameDuration(1/12)
    fill(0)
    rect(0, 0, width(), height())
    fill(1)
    font(path)
    fontSize(380)
    wd, wg = 1000, 1000
    
    for lines in range(1, 8, 1):
        delta = cos(lines + frame / 4)
        fontVariations(wdth = wd * delta, wght = 1000 - wd * delta)
        text("NOPE", (width() / 2, lines * 340 - 360), align="center")

saveImage("_exp/18.gif")