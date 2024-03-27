import fun as F

newPage("A3Landscape")

txt = "ellenzem overall enroller meering norma gil gigue lanea leningen ormar anomalie avaimia roman emerge meer argo enige galinn rearming navigare remi arriero lag gomeril muggen gierig grimoire ungag lezione magazine renni mal zimou lee grummer amme ragioni maurizio mammal emile erin malvagie regina reiver moinen rumourer onanere megan gen avenue ron regulize rivivere lonelier oman romanian aurana online illae elzevir rein gaoler anonimo nez imee lugger gaura minua olgo rameni grane varalle vami mozgov lei ingine lengur livello magii novare elegize reliving nemala malum raring rozen ruolo arrangerer vanille viv enneagonal nilgau arn reveille enllomin irer manen ain alergia lug leigir mama lovelier all marlin aluminio iureiuro logan eviller oiia roller livorno mignon oiva vel vonzza mono mener mage gorilla largo mel organi grouille alogia arruinarlo maaliin maugre gangen linear roger venezuelan mio vivez irreale ongeval mam zvolen lanigerae lira neogaea maire immane emereor nemame omien minagium rouge valvoa mig lana ami rav noie gangi ella ian reunion rolag gervi leur vinnem nummen eiien mignolo aiguaneu ranga egma ren errore evvel male agam viereen mournival ringo zoo rozumie gel miguel legion morling einzelne rami alarmer nemluv nervine zizzing migroleu ignorer vainer lelu loring nugari vaglia mamin emigrar moim gringo gollum"

styles = ["Light", "Regular", "Bold", "Italic", "BoldItalic"]
sizes = [6, 9, 12, 16]

boxH = 150
box = (0, 0, 200, -boxH)

fill(0)
rect(*box)

marge = 40
gutterH = 220
gutterV = 190

def caption(s, x, y):
    font("Menlo")
    fontSize(8)
    text(s, (x, y))
    
with savedState():
    translate(marge, gutterH)
    for style in styles:
        with savedState():
            for size in sizes:
                font(f"Normavaganza-{style}")
                fontSize(size)
                textBox(txt, box)
                translate(0, gutterV)
                caption(f"{size}pt", 0, -(boxH + gutterV)*1.02)
        translate(gutterH, 0)

F.info()
saveImage(f"PDFs/{F.fName()}_{F.timestamp()}.pdf")
