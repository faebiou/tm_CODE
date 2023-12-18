translate(100, 100)

s = 641

idealSize = 400

factor = idealSize / s
print("factor", factor)
print("factor * s", factor * s)


rect(0, 0, s, s)
scale(factor)
fill(1, 1, 0, 0.6)
rect(0, 0, s, s)
