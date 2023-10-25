from fun import *

W = width()
H = height()

fill(0.1)
rect(0, 0, W, H)
fill(0)

myDict = {
    "a": 123,
    "b": 456,
}

print(myDict["a"])
print(myDict.get("b"))
print("a" in myDict)
print(myDict.keys())
print(myDict.values())
print(myDict.items())

