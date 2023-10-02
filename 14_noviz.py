path = BezierPath()
handles = BezierPath()

w = 238
h = 335

ratio = 93
ratio = ratio/100

w_inner = w * ratio*ratio
h_inner = h * ratio
 
outer_curve = 58
outer_curve = outer_curve/100

inner_ratio = 65
inner_ratio = inner_ratio/100

A = w * outer_curve
B = h * outer_curve

C = w * inner_ratio
D = h * inner_ratio

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

fill(0)

translate(width()/2, height()/2)
drawPath(path)