TM = ["Felix", "Nina", "Fabio", "Ben", "Max", "Zhenya", "Mihael", "Pauline", "Ceci"]

shuffle(TM)

desks = {
    1: "Mint",
    2: "",
    3: "",
    4: "Ando",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "Betsy",
    10: "",
    11: "",
    12: ""
    }
    
x = 0
for i in range(12):
    if desks[i+1] == "":
        desks[i+1] = TM[x]
        x += 1
    
        
print(desks)