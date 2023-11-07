import fun as f

def randomBuild(word):
    txt = FormattedString()
    for letter in word:
        txt.font(choice(installedFonts()))
        txt.fontSize(120)
        txt.tracking(80)
        txt.fill(*f.to_rgb(choice(fgC)))
        txt.append(letter)
    return(txt)

fgC = ["#CCFF12", "#FFE600", "#00FFF2", "#FFA9E9", "#FF8888"]
bgC = ["#101D5B", "#5E1D2A", "#0B5629", "#125B7C", "#47182A"]

date = ["11", "25"]

def pattern(bgColor):
    fontSize(190)
    fill(*bgColor, .2)
    blendMode("multiply")    
    for i in range(--29, width()+256, 256):
        for j in range(-90, height(), 192):
            font(choice(installedFonts()))
            text(choice(date), (i,j), align = "center")
    blendMode("normal")

for frame in range(1):
    newPage(1080, 1920)
    frameDuration(1/6)
    HYPE = randomBuild("HYPE")
    AND = randomBuild("AND")
    MEDIA = randomBuild("MEDIA")
    OPEN = randomBuild("OPEN")
    DAY = randomBuild("DAY")

    full = [HYPE, AND, MEDIA, OPEN, DAY]

    bg = f.to_rgb(choice(bgC))
    fill(*bg)
    rect(0,0, width(), height())
    pattern(bg)

    translate(0, 30)

    for word in range(len(full)):
        text(full[word], (width()/2, height() - (word + 1) * 335), align = "center")
        
saveImage("OpenDayThing_FormattedString_3.gif")