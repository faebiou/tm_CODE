path = BezierPath()

w = 248
h = 375

ratio = 93
ratio = ratio/100

w2 = w * ratio*ratio
h2 = h * ratio
 
hP1 = 62
hP1 = hP1/100

hP2 = 71
hP2 = hP2/100


hA = w * hP1
hB = h * hP1

hC = w * hP2
hD = h * hP2

path.moveTo((0, h))
path.curveTo((hA, h), (w, hB), (w, 0))
path.curveTo((w, -hB), (hA, -h), (0, -h))
path.curveTo((-hA, -h), (-w, -hB), (-w, 0))
path.curveTo((-w, hB), (-hA, h), (0, h))
path.reverse()
path.moveTo((0, h2))
path.curveTo((hC, h2), (w2, hD), (w2, 0))
path.curveTo((w2, -hD), (hC, -h2), (0, -h2))
path.curveTo((-hC, -h2), (-w2, -hD), (-w2, 0))
path.curveTo((-w2, hD), (-hC, h2), (0, h2))


fill(0)

translate(500, 500)
drawPath(path)

stroke(None)
font("Menlo")

for point in path.points:
    x, y = point
    d = 10

    # fill(1, 0, 0)
    # oval(x-d/2, y-d/2, d, d)

    # fill(0)
    # text(str(int(x)) + " " + str(int(y)), (x+d, y+d))
