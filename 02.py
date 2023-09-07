newPage(1000, 1000)
n = 24
s = int(width()/n)
g = int((width()-2*s)/s)

for i in range(g, width()-g, s+g):
    for j in range(g, height()-g, s+g):
        fill(random())
        rect(i, j, s, s)

# print(random()*10+20) # random number betwee 20 & 30
# print(dir())
# help(remap)