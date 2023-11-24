import fun as f

def randomBuild(word):
    txt = FormattedString()
    for letter in word:
        txt.font(choice(installedFonts()))
        txt.fontSize(160)
        txt.tracking(80)
        txt.fill(*f.to_rgb(choice(fgC)))
        txt.append(letter)
    return(txt)

fgC = ["#000000"]
bgC = ["#EEEEEE"]                                                                                                                                                                                                                            
# bgC = ["#AAAAAA"]

date = ["NOV", "25"]

def pattern(bgColor):
    fontSize(50)
    fill(*bgColor, 1)
    blendMode("multiply")    
    for i in range(40, width(), 200):
        for j in range(-10, height(), 100):
            font(choice(installedFonts()))
            text(choice(date), (i,j), align = "center")
    blendMode("normal")

for frame in range(48):
    newPage(1080, 1920)
    frameDuration(1/6)
    HYPE = randomBuild("TYPE")
    AND = randomBuild("AND")
    MEDIA = randomBuild("MEDIA")
    OPEN = randomBuild("OPEN")
    DAY = randomBuild("DAY")

    full = [HYPE, AND, MEDIA, OPEN, DAY]

    bg = f.to_rgb(choice(bgC))
    fill(*bg)
    rect(0,0, width(), height())
    pattern(bg)

    translate(0, -303)

    for word in range(len(full)):
        text(full[word], (width()/2, height() - (word + 1) * 242), align = "center")
        
saveImage(f.fName() + ".gif")
saveImage(f.fName() + ".mp4")