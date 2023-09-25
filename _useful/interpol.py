A1 = 290, 740
A2 = 830, 630

B1 = 210, 190
B2 = 320, 240
B3 = 810, 220

# B1 = A1
# B2 = 510, 670
# B3 = A2

fill(None)
stroke(0)

def invLerp(a, b, v):
    return (v - a) / (b - a)

def lerp(a, b, t):
    return a + (b - a) * t
    
t = 100
t = t/100

A = BezierPath()
A.moveTo(A1)
A.lineTo(A2)
A.endPath()
drawPath(A)

B = BezierPath()
B.moveTo(B1)
B.lineTo(B2)
B.lineTo(B3)
B.endPath()
drawPath(B)

len_A = dist(A1, A2)
len_B = dist(B1, B2) + dist(B2, B3)

A_d = len_A / len_B * dist(B1, B2)*2

A_dx = A1[0] + invLerp(A1[0], A2[0], A_d)
A_dy = A2[1] + invLerp(A1[1], A2[1], A_d)
print(A_dx, A_dy)

t = 100
t = t/100

print(A_d)
stroke(1, 0, 0)
oval(A_dx - A_d/2, A_dy - A_d/2, A_d, A_d)