import fun as f
HYPE = "HYPE AND MEDIA"

fgC = ["#CCFF12", "#FFE600", "#00FFF2", "#FFA9E9", "#FF8888"]
bgC = ["#101D5B", "#5E1D2A", "#0B5629", "#125B7C", "#47182A"]

def pattern(bgColor):
    fontSize(120)
    fill(*bgColor, .2)
    blendMode("multiply")
    for i in range(40, width(), 200):
        for j in range(30, height(), 200):
            font(choice(installedFonts()))
            text("#", (i,j), align = "center")
    blendMode("normal")

Y = 1640
delta = 100

def typeSet(sample):
    with savedState():
        for letter in sample:
            fill(*f.to_rgb(choice(fgC)))
            font("Menlo")
            fontSize(72)
            font(choice(installedFonts()))
            text(letter, (width()/2, Y), align = "center")
            translate(0, -delta)

def typeSet_2(sample):
    with savedState():
        for letter in sample:
            fill(*f.to_rgb(choice(fgC)))
            font("Menlo")
            fontSize(72)
            font(choice(installedFonts()))
            text(letter, (width()/2, Y), align = "center")
            translate(delta*.5, 0)

totalFrames = 48
for frame in range(totalFrames):
    newPage(1080, 1920)
    bg = f.to_rgb(choice(bgC))
    fill(*bg)
    rect(0, 0, width(), height())
    fill(0)
    frameDuration(1/4)
    pattern(bg)
    typeSet(HYPE)
    if frame > totalFrames * .25:
        translate(-200, -200)
        typeSet("OPEN")
    if frame > totalFrames * .30:
        translate(400, -600)
        typeSet("DAY")
    if frame > totalFrames * .45:
        translate(-419, -610)
        typeSet_2("25")
    if frame > totalFrames * .5:
        translate(400, 0)
        typeSet_2("11")

saveImage("_exp/openday.gif")