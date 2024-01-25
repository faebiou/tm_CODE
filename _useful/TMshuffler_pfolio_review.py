size("A4")

TM = ["Felix", "Ando", "Nina", "Fabio", "Ben", "Betsy", "Max", "Zhenya", "Mihael", "Mint", "Pauline", "Ceci"]

shuffle(TM)

fs = 32
lh = 2

font("Menlo-Bold")

fontSize(fs)

Y = 80

text("Portfolio Review Pairs", (64, 740))

font("Menlo")

for student in range(0, 11, 2):
    if student != 10:
        text(TM[student] + " & " + TM[student+1], (64, Y))
        translate(0, fs*lh)
    else:
        text(TM[student] + " & " + TM[student+1] + " & Hanna", (64, Y))
        

    
saveImage("../_exp/TMshuffler_pfolio_review.pdf")