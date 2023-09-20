def setup():
    newPage()
    fill(0.1)
    rect(0, 0, width(), height())
    stroke(1)
    fill(None)

def lerp(a, b, t):
    return a + (b - a) * t

def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)

def Handles(a):
    for seg in range(len(a)):
        stroke(0.3)
        strokeWidth(0.1)
        line(a[seg][0], a[seg][1])
        line(a[seg][1], a[seg][2])
        for pts in range(len(a[seg])):
            fill(0, 0, 1) if (pts % (len(a[seg]) - 1) == 0) else fill(1, 0, 0)
            stroke(None)
            midoval(a[seg][pts][0], a[seg][pts][1], 8)

def dothis(i):
    setup()
    stroke(0, 1, 0)
    line(A, B)
    line(B, C)
    t = i / r
    
    # t = 45
    # t = t / 100

    Lx = lerp(A[0], B[0], t)
    Ly = lerp(A[1], B[1], t)

    Rx = lerp(C[0], B[0], 1 - t)
    Ry = lerp(C[1], B[1], 1 - t)

    Cx = lerp(Lx, Rx, t)
    Cy = lerp(Ly, Ry, t)

    midoval(Lx, Ly, 4)
    midoval(Rx, Ry, 4)
    midoval(Cx, Cy, 8)

    line((Lx, Ly), (Rx, Ry))

    stroke(1)
    p = BezierPath()
    L = [[A, B, C]]

    p.beginPath()
    p.moveTo(A)
    p.qCurveTo(B, C)
    p.endPath()

    drawPath(p)
    Handles(L)

A = (160, 720)
B = (780, 830)
C = (860, 150)

r = 100

# -----------------------------------

for fward in range(r):
    dothis(fward)

for bward in range(r):
    dothis(r-bward)

saveImage("qCurve.gif")