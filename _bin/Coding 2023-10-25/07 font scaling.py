unitsPerEm = 1000
shapeSize = 500

pointSize = 400

font("FontTrial/MySquareFiveHundred-Regular.otf")

fontSize(pointSize)

text("A", (100, 100))

stroke(1, 0.5, 0, 0.75)
strokeWidth(8)
fill(None)

rectSize = pointSize * (shapeSize / unitsPerEm)
rect(100, 100, rectSize, rectSize)

print(rectSize)