exec(open("_useful/_fun.py").read())
bg(0.2)

fill(0)

def build(s, d):
    cx = width()/2 
    cy = height()/2
    p = BezierPath()    
    p.oval(cx-s-d/2, cy-s-d/2, d, d)
    p.reverse()
    p.oval(cx+s-d/2, cy+s-d/2, d, d)
    p.reverse()
    p.oval(cx-s-d/2, cy+s-d/2, d, d)
    p.reverse()
    p.oval(cx+s-d/2, cy-s-d/2, d, d)
    drawPath(p)
        
build(95, 579)