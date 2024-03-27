import fun as f

size(2000, 1000)

translate(500, 500)
f.midoval(0, 0, 10)

stroke(0)
fill(None)

D = 776

f.midoval(0, 0, D)

fill(0)
stroke(None)
# f.midoval(D / 2, 0, 10)

for angle2 in range(0, 360, 5):
    angle = 1084
    angleRadians = radians(angle)
    x = cos(angleRadians) * D / 2
    y = sin(angleRadians) * D / 2

    f.midoval(x, y, 10)
    fill(1, 0, 0)

    x = D / 2 * cos(angleRadians)
    y = D / 2 * sin(angleRadians)
    f.midoval(1.3 * x, y, 10)
