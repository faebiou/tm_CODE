HYPE = "HYPE AND MEDIA"

Y = 1600
delta = 100

newPage(1080, 1920)

for letter in HYPE:
    fontSize(72)
    font(choice(installedFonts()))
    text(letter, (width()/2, Y), align = "center")
    translate(0, -delta)