textString = "hey\nwhat's up"
txt = FormattedString()

txt.fontSize(50)

for char in textString:
    txt.font(choice(installedFonts()))
    txt.append(char)
    
textBox(txt, (100,100,600, 700))