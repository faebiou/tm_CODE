# import f
# watch out for globals !
path = BezierPath()
handles = BezierPath()
translate(500, 500)


def circle(centerX, centerY, diameter):
    radius = diameter / 2
    x = centerX - radius
    y = centerY - radius
    oval(x, y, diameter, diameter)


def counter(w, h, prop):

    prop = prop / 100

    handle1 = w * prop
    handle2 = h * prop

    path.moveTo((0, h))
    path.curveTo((handle1, h), (w, handle2), (w, 0))
    path.curveTo((w, -handle2), (handle1, -h), (0, -h))
    path.curveTo((-handle1, -h), (-w, -handle2), (-w, 0))
    path.curveTo((-w, handle2), (-handle1, h), (0, h))

    Handles(w, h, handle1, handle2)


def Handles(w, h, handle1, handle2):
    handles.moveTo((-handle1, h))
    handles.lineTo((handle1, h))
    handles.moveTo((w, handle2))
    handles.lineTo((w, -handle2))
    handles.moveTo((handle1, -h))
    handles.lineTo((-handle1, -h))
    handles.moveTo((-w, -handle2))
    handles.lineTo((-w, handle2))


def Points():
    fill(1, 0, 0)
    stroke(None)
    for point in path.points:
        x, y = point
        circle(x, y, 5)


counter(328, 413, 59)
counter(-210, 393, 83)

stroke(0)

fill(0.7)
drawPath(path)

fill(None)
drawPath(handles)

Points()