fill(0, 0, 1)
rect(0, 0, 670, 690)
p = BezierPath()

p.moveTo((280, 900))
p.lineTo((110, 130))
p.lineTo((850, 240))
# handle 1 xy, handle 2 xy, end point
p.curveTo((800, 480), (941, 660), (810, 842))
p.closePath()

p.moveTo((820, 310))
p.lineTo((210, 180))
p.lineTo((310, 820))
p.lineTo((750, 810))
p.closePath()

fill(1, 0, 0)
stroke(0)
strokeWidth(10)
drawPath(p)