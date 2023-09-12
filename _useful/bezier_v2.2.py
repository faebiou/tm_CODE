newPage(1000,1000)
fill(.1)
rect(0,0,width(),height())

def midoval(x,y,r):
    oval(x-r/2,y-r/2,r,r)
    
stroke(1)
strokeWidth(1)
fill(None)

char = "NICE\nSHIT"
pt = 330

x = width()/2
y = height()/2 + pt/4

fontName = "Menlo-Regular"

font(fontName)
fontSize(pt)
text(char, (x, y), align="center")
path = BezierPath()
glyphPath = BezierPath()
glyphPath.text(char, font=fontName, fontSize=pt, align="center")
path.appendPath(glyphPath)

strokeWidth(0)

fill(0,1,0)
translate(x,y)

for contours in range(len(path)):
    for segments in range(len(path[contours])):
        for coordinate in range(len(path[contours][segments])):
            oval(path[contours][segments][coordinate][0]-2,path[contours][segments][coordinate][1]-2,4,4)
                    