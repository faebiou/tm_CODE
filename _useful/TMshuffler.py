size("A4")

TM = ["Felix", "Ando", "Nina", "Fabio", "Ben", "Betsy", "Max", "Zhenya", "Mihael", "Mint", "Pauline", "Ceci"]

shuffle(TM)

fs = 32
lh = 2
font("Menlo")
fontSize(fs)

for student in range(len(TM)):
    text(TM[student] + " → " + TM[student-1], (64, 60))
    translate(0, fs*lh)
    
saveImage("../_exp/TMshuffler_3.pdf")