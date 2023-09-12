# ELOKESZULETEK —————————————————————————
# uj oldal
newPage(1000,1000)
# hatter szine
fill(.1)
# hatter rajzolas
rect(0,0,width(),height())

# sajat fuggvenyem ami x,y poziba rajzol egy r sugaru kort kozeprol szamitva – Matek!
def midoval(x,y,r):
    oval(x-r/2,y-r/2,r,r)
    
# feher stroke
stroke(1)
# 1 pt(?) vastag
strokeWidth(1)
# ures
fill(None)

# szoveg – lehet baszakodni vele
char = "NICE\nSHIT"
# betumeret – ezzel is lehet baszakodni
pt = 330

# szoveg kiirasahoz szukseges pozik
x = width()/2
# a pt/4-et siman lehet vmilyen ertekkel helyettesiteni, de egesz jol belovi kozepre
y = height()/2 + pt/4

# ezt at lehet irni, de nem mindig konnyu megtalalni a font nevet
fontName = "Menlo-Regular"

# SZOVEGSZEDES ——————————————————————————

# itt valasztjuk ki a fontot
font(fontName)
# itt allitjuk be a betumeretet
fontSize(pt)
# itt rajzoljuk ki a feher szoveget
text(char, (x, y), align="center")
# ez az egesz Bezierunk – mint egy Group Illustratorban
path = BezierPath()
# ezek a kulon elemek, mintha Ungroupolnank, kb
glyphPath = BezierPath()
# ez alakitja at fontbol formava
glyphPath.text(char, font=fontName, fontSize=pt, align="center")
# ez pedig hozzaadja a csoporthoz
path.appendPath(glyphPath)

# KONTROLLPONTOK  ———————————————————————

# a feher formak megvannak mar, most mar csak ki kell rakni a kontrollpontokat
# a stroke meg feher, szoval eloszor kikapcsoljuk:
strokeWidth(0)
# aztan nem volt fill, szoval rakunk neki egy zoldet
# a szamok normalizalt RGB ertekek, tehat a 0 az 0, de az 1 meg 255-nek felel meg
# a tobbit ki lehet matekolni, ekeppen: fill(R/255, G/255, B/255) – ahol az R, G, es B nyilvan a szinetek megfelelo ertekei ;)
fill(0,1,0)
# ezzel a sorral egyeztetjuk a pontjaink koordinatait a szovegunk koordinatajaval
translate(x,y)
# a kovetkezo ciklusok lenyege az hogy vegyunk sorban minden szegmenst es a pontjait – ez lehet egy kicsit tul nagy falat elsore, de szivesen belemegyek reszletekbe ha erdekel :D – a lenyeg hogy megyen!
for contours in range(len(path)):
    for segments in range(len(path[contours])):
        for coordinate in range(len(path[contours][segments])):
            oval(path[contours][segments][coordinate][0]-2,path[contours][segments][coordinate][1]-2,4,4)
                    