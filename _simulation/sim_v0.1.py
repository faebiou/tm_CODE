# blank
exec(open("../_useful/_fun.py").read())

fs = 500
res = 300

fontSize(fs)
text("Aa", (width()/2, 350), align = "center")

img = "ref.png"
saveImage(img)

w, h = imageSize(img)
step = 4

newPage()
for x in range(w):
    for y in range(h):
        c = imagePixelColor(img, (x, y))
        if c:
            L = 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]
            fill(*c)
            midoval(x, y, .5)

saveImage("test.pdf")