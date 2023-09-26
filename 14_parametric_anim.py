def Handles():
    fill(None)
    stroke(0)
    handles.moveTo((-A, h))
    handles.lineTo((A, h))
    handles.moveTo((-C, h_inner))
    handles.lineTo((C, h_inner))
    handles.moveTo((-A, -h))
    handles.lineTo((A, -h))
    handles.moveTo((-C, -h_inner))
    handles.lineTo((C, -h_inner))
    handles.moveTo((w, B))
    handles.lineTo((w, -B))
    handles.moveTo((w_inner, D))
    handles.lineTo((w_inner, -D))
    handles.moveTo((-w, B))
    handles.lineTo((-w, -B))
    handles.moveTo((-w_inner, D))
    handles.lineTo((-w_inner, -D))
    drawPath(handles)
    stroke(None)

def OnOffCurves(x, y, r):
    oval(x-d/2, y-d/2, d, r)

def Coordinates(x, y, d):
    fill(0.7)
    text(str(int(x)) + " " + str(int(y)), (x, y+d))

w = 242
h = 365

def path_anim():
    path.moveTo((0, h))
    path.curveTo((A, h), (w, B), (w, 0))
    path.curveTo((w, -B), (A, -h), (0, -h))
    path.curveTo((-A, -h), (-w, -B), (-w, 0))
    path.curveTo((-w, B), (-A, h), (0, h))
    path.reverse()
    path.moveTo((0, h_inner))
    path.curveTo((C, h_inner), (w_inner, D), (w_inner, 0))
    path.curveTo((w_inner, -D), (C, -h_inner), (0, -h_inner))
    path.curveTo((-C, -h_inner), (-w_inner, -D), (-w_inner, 0))
    path.curveTo((-w_inner, D), (-C, h_inner), (0, h_inner))
    drawPath(path)

numframes = 60
scale = 3

for frame in range(numframes):
    if frame <= numframes/2:
        w += frame * scale
    else:
        w += (frame - numframes) * scale - scale
    
    ratio = 93
    ratio = ratio/100

    w_inner = w * pow(ratio, 2)
    h_inner = h * ratio
 
    outer_curve = 58
    outer_curve = outer_curve/100

    inner_curve = 66
    inner_curve = inner_curve/100

    A = w * outer_curve
    B = h * outer_curve

    C = w * inner_curve
    D = h * inner_curve
    
    path = BezierPath()
    handles = BezierPath()

    newPage()
    frameDuration(1/numframes)
    fill(1)
    rect(0,0,width(), height())
    
    fill(0)
    translate(width()/2, height()/2)
    path_anim()

    fill(0)
    stroke(None)
    font("Menlo")

    Handles()

    counter = 0
    for point in path.points:
        counter = counter + 1
        d = 10
        x, y = point
        if counter > 13:
            fill(0, 0, 1)
        else:
            fill(1, 0, 0)
        OnOffCurves(x, y, d)
        Coordinates(x, y, d)
        
saveImage("_exp/yay.gif")
