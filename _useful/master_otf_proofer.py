import os
import fun as f

OTFs = []

for master_otf in os.listdir():
    if master_otf.endswith(".otf"):
        OTFs.append(master_otf)

chars = """
whatever text
you would like
to see
"""


for OTF in range(len(OTFs)):
# for OTF in range(1):
    newPage()
    frameDuration(1/3)
    f.bg(1)
    
    fill(0)
    
    fs = 24
    txt = FormattedString()
    for c in chars:
    
        if fontContainsGlyph(c):
            txt.append(c, font = OTFs[OTF], fontSize = fs, fill = (0, 0, 0))
        else:
            fill(1, 0, 0)
            txt.append(c, font = "Menlo", fontSize = fs / 2, fill = (1, 0, 0))

    text(txt, (100, 900))
    fill(0)
    fontSize(10)
    f.info_extra(OTFs[OTF])

saveImage(f.fName() + ".gif")