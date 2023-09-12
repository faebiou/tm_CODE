newPage("A4")
txt = "Hambruges"

ml = 50
mt = 100

x, y = ml, height()-mt

fs = 92

font("Menlo")

fontSize(fs)
text(txt, (x, y))

textWidth, textHeight = textSize(txt)

stroke(1, 0, 0)
for metric in (0, fontDescender(), fontAscender(), fontXHeight(), fontCapHeight()):
    line((x, y+metric), (x+textWidth, y+metric))

asc  = round(fontAscender(),2)
desc = round(fontDescender(),2)
xh   = round(fontXHeight(),2)
caps = round(fontCapHeight(),2)

# captions

font("Menlo")
fontSize(8)
stroke(None)
fill(0)

xcaption = ml
ycaption = height()-1.5*mt

lh = 12

text("x = "+str(xh), (xcaption, ycaption-0*lh))
text("a = "+str(asc), (xcaption, ycaption-1*lh))
text("d = "+str(desc), (xcaption, ycaption-2*lh))
text("c = "+str(caps), (xcaption, ycaption-3*lh))

# a = installedFonts()
# print(*a, sep="\n")