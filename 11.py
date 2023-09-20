exec(open("_useful/_fun.py").read())
# light first contour, first point x
a = 10
# bold first contour, first point x
b = 60
# interpolation factor
f = 1

distance = b - a

travelDistance = f * distance

c = a + travelDistance

print(c)

c = a + f * (b - a)