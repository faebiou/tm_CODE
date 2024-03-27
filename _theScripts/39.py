size(2000, 1000)

def graph(s):
    S = int(100*s)
    oval(0, 0, S, S)    
    W = int(width()/s)*4
    H = int(height()/s)*4
    for i in range(0, H, S):
        line((i, 0), (i, H))
        for j in range(0, W, S):
            line((0, j), (W, j))

blendMode("multiply")

stroke(0)
fill(0)

s = 2

graph(s)


stroke(1, 0, 0)
fill(1, 0, 0)

s = 170/100

scale(s)
strokeWidth(1/s)

graph(s)
