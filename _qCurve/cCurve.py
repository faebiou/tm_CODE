fill(0.1)
rect(0, 0, width(), height())
stroke(1)
fill(None)


def lerp(a, b, t):
    return a + (b - a) * t


def qerp(a, b, t):
    return a + (b - a) * t


def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)


def Handles(a):
    for seg in range(len(a)):
        stroke(0.3)
        strokeWidth(0.1)
        line(a[seg][0], a[seg][1])
        line(a[seg][2], a[seg][3])
        for pts in range(len(a[seg])):
            fill(0, 0, 1) if (pts % (len(a[seg]) - 1) == 0) else fill(1, 0, 0)
            stroke(None)
            midoval(a[seg][pts][0], a[seg][pts][1], 8)


A = (110, 755)
B = (640, 860)
C = (830, 330)
D = (470, 90)

stroke(0, 1, 0)

# -----------------------------------

line(A, B)
line(C, D)

t = 45
t = t / 100

line(B, C)

# -----------------------------------

L1x = lerp(A[0], B[0], t)
L1y = lerp(A[1], B[1], t)

R1x = lerp(C[0], B[0], 1 - t)
R1y = lerp(C[1], B[1], 1 - t)

C1x = lerp(L1x, R1x, t)
C1y = lerp(L1y, R1y, t)

midoval(L1x, L1y, 4)
midoval(R1x, R1y, 4)

line((L1x, L1y), (R1x, R1y))
midoval(C1x, C1y, 4)

# -----------------------------------

L2x = lerp(B[0], C[0], t)
L2y = lerp(B[1], C[1], t)

R2x = lerp(C[0], D[0], t)
R2y = lerp(C[1], D[1], t)

C2x = lerp(L2x, R2x, t)
C2y = lerp(L2y, R2y, t)

midoval(L2x, L2y, 4)
midoval(R2x, R2y, 4)

line((L2x, L2y), (R2x, R2y))
midoval(C2x, C2y, 4)

# # -----------------------------------

line((C1x, C1y), (C2x, C2y))

Cx = lerp(C1x, C2x, t)
Cy = lerp(C1y, C2y, t)

midoval(Cx, Cy, 8)

# -----------------------------------

stroke(1)
p = BezierPath()
L = [[A, B, C, D]]

p.beginPath()
p.moveTo(A)
p.curveTo(B, C, D)
p.endPath()

drawPath(p)
Handles(L)
