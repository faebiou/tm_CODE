total = 30

f = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 0), (0, 1, 1), (1, 0, 1)]

for i in range(total):
    newPage(1080, 1920)
    current = i / total
    fill(*f[0])
    rect(0, height(), width(), -height() * (1 - current))
    fill(*f[3])
    rect(0, 0, width(), height() * current)

for i in range(total + 1, 2 * total, 1):
    newPage(1080, 1920)
    current = i / total
    fill(*f[3])
    rect(0, height(), width(), -height() * current)
    fill(*f[0])
    rect(0, 0, width(), -height() * (1 - current))

saveImage("_exp/62.gif")