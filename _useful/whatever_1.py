from importlib import reload
import _fun as fun
reload(fun)

newPage(1000, 1700)
fontSize(446)
font("/Users/user/Library/Fonts/Bagdolldisplay-Regular.otf")

vertical_offset = 90

position = (width()/2, height()/2)

text("One", (width()/2, height()/2 - 6*vertical_offset), align = "center")
text("Two", (width()/2, height()/2 - vertical_offset), align = "center")
text("Tri", (width()/2, height()/2 + 4*vertical_offset), align = "center")

fill(1, 0, 0)
#     x    y    w   h
#   ( x    y )  w   h
#     x    y    w   h?
rect(*position, 10, 10)

# loop animations / sound
# instagram posts … maybe?
# modifying outlines
# proofing !!
# animation / showing ? !
# putting the FUN back in functions
# parentheses or how you spell that
# yay
# pictures ! import ! scans :/
# yay x2
# variable fonts !