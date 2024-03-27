exec(open("_useful/_fun.py").read())
bg(0.2)

fill(0)


def circle(x, y, d):
    r = d / 2
    oval(x - r, y - r, d, d)


d = 23

for i in range(2 * d, width() - 2 * d, int(width() / d)):
    for j in range(2 * d, height() - 2 * d, int(height() / d)):
        fill(1 - random() * 0.5)
        circle(i, j, d)
        fill(1)
        fontSize(5)
        text(str(i) + " " + str(j), (i-d, j-d))
        
