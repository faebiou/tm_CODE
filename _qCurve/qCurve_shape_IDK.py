fill(.1)
rect(0, 0, width(), height())

def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)

def lerp(a, b, t):
    return a + (b - a) * t

def quad(A, B, C, f):
    return ((1 - f) ** 2) * A + 2 * f * B * (1 - f) + (f ** 2) * C

r = 10
p = BezierPath()

P0 = 200, 230
P1 = 540, 770
P2 = 780, 470
P3 = 500, 200

fill(1)
midoval(*P0, r)
midoval(*P1, r)
midoval(*P2, r)
midoval(*P3, r)

fill(None)
stroke(1)

p.moveTo(P0)
p.lineTo(P1)
p.qCurveTo(P2, P3)
p.endPath()

t = 28
t = t / 100

x1 = lerp(P0[0], P1[0], t)
y1 = lerp(P0[1], P1[1], t)

midoval(x1, y1, r)

x2 = quad(P1[0], P2[0], P3[0], t)
y2 = quad(P1[1], P2[1], P3[1], t)

midoval(x2, y2, r)
drawPath(p)