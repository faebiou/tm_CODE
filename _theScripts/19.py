txt = "Hello there is some text. " * 30

fill(.3)
rect(0, 0, width(), height())
fill(0)

fontSize(29)
font("Helvetica")

delta = 25
box1 = (50, 50, width()/2 - delta, 500)
box2 = (width()/2 + delta, 50, 400, 499)

fill(.5)
rect(*box1)
rect(*box2)

fill(0)



remainder = textBox(txt, box1)

rest = textBox(remainder, box2)

print(remainder)