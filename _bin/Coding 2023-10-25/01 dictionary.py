myDict = {"a": 123, "b": 456}

print(myDict)  # --> {'a': 123, 'b': 456}

print(myDict["a"])  # --> 123
print(myDict["b"])  # --> 456
# print(myDict["c"])
print(myDict.get("a"))  # --> 123
print(myDict.get("c"))  # --> None
print("a" in myDict)  # --> True
print("q" in myDict)  # --> False
print()
myDict["d"] = 7654  # to add an item
print(myDict)
del myDict["b"]  # to remove an item
print(myDict)
print(myDict.keys())
print(myDict.values())
print(myDict.items())
