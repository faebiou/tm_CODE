def splitRectH(r, f):
    x, y, w, h = r
    return (x, y, f * w, h), (x + f * w, y, (1 - f) * w, h)

def splitRectV(r, f):
    x, y, w, h = r
    return (x, y, w, f * h), (x, y + f * h, w, (1 - f) * h)


def splitRecursive(r, level):
    if level > 0:
        if level % 2:
            r1, r2 = splitRectH(r, 0.25 + random() / 2)
        else:
            r1, r2 = splitRectV(r, 0.25 + random() / 2)
        splitRecursive(r1, level - 1)
        splitRecursive(r2, level - 1)
    else:
        rect(*r)


r = (100, 100, 500, 600)

stroke(0)
fill(None)
splitRecursive(r, 5)

# # rect(*r)

# fill(0.5, 0.5)

# r2, r3 = splitRectV(r, 0.6)

# rect(*r2)
# fill(0.25, 0.5)

# rect(*r3)
