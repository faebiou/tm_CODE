def graph(s):
    W = int(width() / s)
    H = int(height() / s)
    for i in range(0, H, 100):
        line((i, 0), (i, H))
        for j in range(0, W, 100):
            line((0, j), (W, j))


font("Menlo")
fontSize(24)

size = 200
target = 500
factor = target / size

blendMode("multiply")
    
fill(0)
stroke(None)
text("initial size: " + str(size), (50, height() - 50))

fill(1, 0, 0)
stroke(1, 0, 0)
rect(100, 100, size, size)
graph(1)

fill(0)
stroke(None)
text("target size: " + str(target), (50, height() - 100))
text("factor: " + str(factor), (50, height() - 150))

scale(factor)

fill(0, 0, 1)
stroke(0, 0, 1)
rect(100/factor, 100/factor, size, size)
graph(factor)
