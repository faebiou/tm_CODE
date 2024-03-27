import fun

# FIX equilateral triangle, sort of
def triangle(x, y, a):
    temp = (2 / sqrt(3))
    h = a * temp/1.7
    polygon((x - h / 2, y - h / 2), (x, y + h / 2), (x + h / 2, y - h / 2))

rotate(0, center=(500, 500))

fill(*fun.to_rgb("##53f559"))
triangle(500, 500, 870)

fill(0)
fun.midoval(500,500, 10)
