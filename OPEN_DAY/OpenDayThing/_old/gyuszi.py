import fun as f
sample = "NINCSHELY"

X = 200
delta = 190

for frame in range(12):
    newPage(1920, 1080)
    f.bg(0)
    fill(*f.to_rgb("#B1B7A9"))
    frameDuration(1/2)
    for letter in sample:
        font("Menlo")
        fontSize(120)
        font(choice(installedFonts()))
        text(letter, (X, height()/2), align = "center")
        translate(delta, 0)

saveImage("gyuszi_2.gif")