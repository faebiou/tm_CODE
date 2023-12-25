def splitRectH(r, f):
    x, y, w, h = r
    return (x, y, f * w, h), (x + f * w, y, (1 - f) * w, h)

def splitRectV(r, f):
    x, y, w, h = r
    return (x, y, w, f * h), (x, y + f * h, w, (1 - f) * h)

def isItWide(x, y, w, h):
    if w/h > 1:
        return 1
    else:
        return 0

def splitRecursive(r, level):
    if level > 0:
        if isItWide(*r):
            r1, r2 = splitRectH(r, 0.25 + random() / 2)
        else:
            r1, r2 = splitRectV(r, 0.25 + random() / 2)
        splitRecursive(r1, level - 1)
        splitRecursive(r2, level - 1)
    else:
        rect(*r)

size(1920, 1080)
r = (0,0, width(), height())

stroke(0)
fill(None)
splitRecursive(r, 5)

# # rect(*r)

# fill(0.5, 0.5)

# r2, r3 = splitRectV(r, 0.6)

# rect(*r2)
# fill(0.25, 0.5)

# rect(*r3)
