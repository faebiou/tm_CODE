import random
import fun as f
import random as r

Regular = "Normavaganza Text Regular"
Bold = "Normavaganza Text Regular Bold"
Italic = "Normavaganza Text Italic"

# first weight always = 1
# can have as many weights as desired
fonts = [Regular, Bold, Italic]
# weights[0] refers to fonts[1], weights[1] refers to fonts[2] and so on … 
# 1/10 means every 10th word is Bold, 1/20 means every 20th word is Italic in this case
weights = [1/10, 1/20]
fs = 14

txt = '''\
maiori mellemrum zorino lamella mamu alma erm anil veau nonae malum nevezme arm leon rouva vaner vana remover loaner miller eleanore ranarium rameno moi moralize lonnie ilamo name annen mueller amene melon anular allemal eleanor amelie armoire river amine momzer llera meille rulle riverain vola envirollen avenue animae run ruiner mara vainaa amor vivere noon enero merui rio monille mino larva love mini amen oar avale ene oliver variole vallan umana lueur nimia voel unir riviin mailla levi anima roll lenin aviven rene lianne mira lize ulmin miliona rivaal loze iaver nuera vin verval rommelen narazila mollio lalo viola minima mazze aurelian analemma rizzo numeroon naiver neo lerner amove luova vomere llum nona veniam muro ollie olivera earl ozono ano unelmani valuu oral vivien remi vin rue real verla immune naamaa loven onnozelaar uranium neverim annoia venner mel alarmar umrze voi milieu eilen nan alle lener emile mimi zaveziem anna morirme oom mooi orion nei nezmenil arnie elue molo overleve min ellene arriere laurel millionaire vernon nevelni unroll oluelle vine level nellie zoenen veimme vaaranna mariner volano mammon varir ouvrirai envier rollerne zoeal muzzier romanorum emeli revile elleni muoiano numrene inion lea rem moneron reza annuel avranno nimi zoe aveu
'''

gutter = 370
box1 = (70, 110, 300, 630)

s = 4

newPage("A3Landscape")
with savedState():
    font(Regular)
    
    fontSize(fs)
    textBox(txt, box1)

    translate(gutter, 0)

    font(Bold)
    fontSize(fs)
    textBox(txt, box1)

    translate(gutter, 0)

    words = txt.split(" ")
    textBox(f.insert_multiple(words, fonts, fs, weights), box1)

f.info()

#saveImage(f"PDFs/proofer_both_{f.timestamp_hour()}.pdf")


