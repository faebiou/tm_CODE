path = "/Users/user/Creative Cloud Files/TYPE/_MISC/mutatorSans-master/MutatorSans.ttf"

font(path)
fontSize(180)

wd, wg = 1000, 0
for lines in range(5):
    delta = sin(lines / 4)
    fontVariations(wdth = wd * delta, wght = wg * delta)
    text("NOPE", (width() / 2, lines * 182 + 70), align="center")