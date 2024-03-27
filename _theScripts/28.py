def midoval(x, y, r):
    oval(x - r / 2, y - r / 2, r, r)


newPage(1080, 1920)

fill(0)
rect(0, 0, width(), height())
fill(0, 1, 0.3)

im = ImageObject()

r = 20
step = 20

with im:
    fill(0, 1, 0.3)
    rect(90, 50, 50, 50)

im.gaussianBlur(3)
x, y = im.offset()


image(im, (10 + x, 20 + y))
