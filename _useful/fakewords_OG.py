from time import *

cons = "bcdfghjklmnpqrstvwxz"
vows = "aeiou"

size("A4")

# setup
def construct(n):
    word = ""
    for c in range(n):
        rC = randint(0, len(cons)-1)
        rV = randint(0, len(vows)-1)
        if c % 2:
            word += cons[rC]
        else:
            word += vows[rV]
    return word

# margin & vertical ratio
marge = 70
ratio = .9

# your font goes here
font("Menlo")
fs = 12
fontSize(fs)
lineHeight(fs * 1.2)

# parameters
minLetters = 3
maxLetters = 8
thisManyWords = 1000

txt = ""
for i in range(thisManyWords):
    r = randint(minLetters, maxLetters)
    txt += construct(r) + " "
    
textBox(txt, (0 + marge, 0 + marge * ratio + 12, width() - marge * 2, height() - marge * 2 * ratio))

font("Menlo")
fontSize(5)

t = ctime()

text("min: " + str(minLetters) + " | max: " + str(maxLetters) + " | word count: " + str(thisManyWords) + " | " + str(t), (marge/2, marge/2))

# save a document with the current time as its name
saveImage(str(ctime()) + ".pdf")