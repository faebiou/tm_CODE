fill(random()*.9, random()*.9, random()*.9)
rect(0, 0, width(), height())

fill(random()*.3, random()*.3, random()*.3)

fontSize(330)
font("ComicSansMS-Bold")


txt = """WHAT
{THE}
SHIT
"""
lineHeight(323)
tracking(43)
text(txt, (width()/2, 702), align = "center")



print(len(installedFonts()))