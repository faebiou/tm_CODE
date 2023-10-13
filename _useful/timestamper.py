import time as t

def timestamp():
    Y = str(t.localtime()[0] - 2000)
    M = str(t.localtime()[1])
    D = str(t.localtime()[2])
    H = str(t.localtime()[3])
    M = str(t.localtime()[4])
    S = str(t.localtime()[5])
    return Y + "_" + M + "_" + D + "__" + H + "_" + M + "_" + S
    
print(timestamp())