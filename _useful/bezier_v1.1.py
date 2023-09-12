newPage(1000,1000)
fill(.1)
rect(0,0,width(),height())

A = [ [ [ 100, 100 ],[ 380, 110 ],[ 520, 240 ],[ 500, 500 ] ],
      [ [ 500, 500 ],[ 400, 300 ],[ 250, 500 ],[ 100, 300 ] ],
      [ [ 100, 300 ],[ 300, 800 ],[ 600, 800 ],[ 800, 600 ] ],
      [ [ 800, 600 ],[ 600, 450 ],[ 600, 200 ],[ 900, 100 ] ] ]

Variable([
    dict(name="t", ui = "Slider",
        args = dict(
            value = .5,
            minValue = 0,
            maxValue = 1
            ))
    ], globals())

def midoval(x,y,r):
    oval(x-r/2,y-r/2,r,r)

def lerp(a, b, t):
    return a + (b - a) * t

def cube(P0, P1, P2, P3, f):
    return (1-f)**3*P0 + f*P1*(3*(1-f)**2) + P2*(3*(1-f)*f**2) + P3*f**3

stroke(1)
strokeWidth(1)
fill(None)

def DrawThis(a):
    p = BezierPath()
    for seg in range(len(a)):
        p.beginPath()
        p.moveTo(a[seg][0])
        p.curveTo(a[seg][1], a[seg][2], a[seg][3])
        p.endPath()
    drawPath(p)

def Handles(a):
    for seg in range(len(a)):   
        stroke(1)
        strokeWidth(0.1)
        line(a[seg][0],a[seg][1])
        line(a[seg][2],a[seg][3])
        for pts in range(len(a[seg])):
            fill(0,0,1) if (pts % (len(a[seg])-1) == 0) else fill(1,0,0)
            stroke(None)
            midoval(a[seg][pts][0],a[seg][pts][1],8)
         
def Coordinates(a):
    offset = 5
    for seg in range(len(a)):
        for pts in range(len(a[seg])):
            c = "(" + str(A[seg][pts][0]) + ", " + str(a[seg][pts][1]) + ")"
            fill(0,0,1) if (pts % (len(a[seg])-1) == 0) else fill(1,0,0)
            text(c, (a[seg][pts][0]+offset, a[seg][pts][1]+offset))

DrawThis(A)
Handles(A)
Coordinates(A)


def super_cube(a):
    fill(0,1,0)
    stroke(None)
    for seg in range(len(a)):
        xc = cube(a[seg][0][0],a[seg][1][0],a[seg][2][0],a[seg][3][0],t)
        yc = cube(a[seg][0][1],a[seg][1][1],a[seg][2][1],a[seg][3][1],t)
        midoval(xc,yc,5)
        strokeWidth(.1)
        stroke(1)
        line((a[seg][0][0],a[seg][0][1]),(xc,yc))
        line((a[seg][3][0],a[seg][3][1]),(xc,yc))        
       
       
super_cube(A)