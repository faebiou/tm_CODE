txt = FormattedString()
txt.fontSize(50)

OGfont = choice(installedFonts())
txt.font(OGfont)
txt.align("center")
txt.append("Hello wwrodl akd slnga akdjsgh lkjahfg  akfjlgho")

txt.font(choice(installedFonts()))
txt.fill(random(), random(), random())
txt.align("center")
txt.append("WAIT WHAT")

txt.font(OGfont)
txt.fill(0)
txt.align("center")
txt.append(" kfhgo asdkjg asdkjghl sdkluyab adskugha kuagsd. Right?")

boxW = 460
textBox(txt, ((width() - boxW) / 2, 100, boxW, 720))
