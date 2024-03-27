def circle(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)

bez = BezierPath()

fs = 1000

for frame in range(12):
    newPage(1080, 1920)

    bez.text(
        "B",
        (width() / 2, height() / 2 - fs / 4),
        font="Menlo",
        fontSize=fs,
        align="center",
    )

    bez.rect(-40, 850, 760, 410)

    steps = 30
    blendMode("screen")

    for i in range(-steps, width() + steps, steps):
        for j in range(-steps, height() + steps, steps):
            if bez.pointInside((i, j)):
                fill(1, 0, 0)
            else:
                fill(0, 0, 1)
            circle(i, j, steps * 1.6 * frame/10)

for frame in range(12):
    newPage(1080, 1920)

    bez.text(
        "B",
        (width() / 2, height() / 2 - fs / 4),
        font="Menlo",
        fontSize=fs,
        align="center",
    )

    bez.rect(-40, 850, 760, 410)

    steps = 30
    blendMode("screen")

    for i in range(-steps, width() + steps, steps):
        for j in range(-steps, height() + steps, steps):
            if bez.pointInside((i, j)):
                fill(1, 0, 0)
            else:
                fill(0, 0, 1)
            circle(i, j, steps * 1.6 * (12-frame)/10)
            
saveImage("_exp/32.gif")