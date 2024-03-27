exec(open("_useful/_fun.py").read())

bg(.1)

fill(0)
numCells = 10
cellSize = 80
cellDistance  = 100

# translate((cellDistance-cellSize)/2, (cellDistance-cellSize)/2)

for i in range(numCells):
    x = i * cellDistance
    for j in range(numCells):
        y = j * cellDistance
        if(i > 2 and j < 5):
            fill(.2)
        else:
            fill(.3)
        rect(x, y, cellSize, cellSize)