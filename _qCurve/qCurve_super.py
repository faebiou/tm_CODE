# quads!

newPage(1000, 1000)
fill(0.1)
rect(0, 0, width(), height())

one = (196, 204)
two = (420, 494)
three = (120, 620)
four = (796, 696)
five = (920, 160)

A = [
    [one, [450, 290], two],
    [two, [210, 460], three],
    [three, [480, 890], four],
    [four, [590, 460], five],
]

t = 48
t = t / 100


def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)


def lerp(a, b, t):
    return a + (b - a) * t


def quad(P0, P1, P2, f):
    return ((1 - f) ** 2) * P0 + 2 * f * P1 * (1 - f) + (f ** 2) * P2


stroke(1)
strokeWidth(1)
fill(None)


def DrawThis(a):
    p = BezierPath()
    for seg in range(len(a)):
        p.beginPath()
        p.moveTo(a[seg][0])
        p.qCurveTo(a[seg][1], a[seg][2])
        p.endPath()
    drawPath(p)


def Handles(a):
    for seg in range(len(a)):
        stroke(1)
        strokeWidth(0.1)
        line(a[seg][0], a[seg][1])
        line(a[seg][1], a[seg][2])
        for pts in range(len(a[seg])):
            fill(0, 0, 1) if (pts % (len(a[seg]) - 1) == 0) else fill(1, 0, 0)
            stroke(None)
            midoval(a[seg][pts][0], a[seg][pts][1], 8)


DrawThis(A)
Handles(A)


def super_quad(a):
    fill(0, 1, 0)
    stroke(None)
    for seg in range(len(a)):
        xc = quad(a[seg][0][0], a[seg][1][0], a[seg][2][0], t)
        yc = quad(a[seg][0][1], a[seg][1][1], a[seg][2][1], t)
        stroke(0)
        midoval(xc, yc, 15)
        strokeWidth(0.1)
        stroke(1)
        line((a[seg][0][0], a[seg][0][1]), (xc, yc))
        line((a[seg][2][0], a[seg][2][1]), (xc, yc))


super_quad(A)
