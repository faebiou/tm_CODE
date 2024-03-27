import string
from datetime import datetime

timeNow = str(datetime.now())

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase

output = ""

for uc in uppercase:
    for lc in lowercase:
        output += uc + lc + " "

f = choice(installedFonts())
# f = "Comic Sans MS"

pagenumber = 0

while output:
    newPage("A4Landscape")

    font(f)
    fontSize(50)

    margin = 20
    box = (margin, margin, width() - margin * 2, height() - margin * 2)

    fill(0)
    stroke(None)
    output = textBox(output, box)
    
    font("Menlo")
    fontSize(12)
    text(str(pagenumber) + " | " + f + " | " + timeNow, (margin, 20))
    
    pagenumber += 1
    
    
    
    
    