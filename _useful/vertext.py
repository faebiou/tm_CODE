# defining a function that sets a word vertically
# word is a string, x and y _start are the coordinates
# lineheight is the distance between letters
# alignment can be center, left, or right
def vertext(w, x_start, y_start, line_height, alignment):
   
    # loop through the word
    for letter in range(len(w)):
        # place letters one by one in the correct position
        text(w[letter], (x_start, y_start - (letter * line_height)), align = alignment)


# page size
newPage(1080, 1920)

# setting the font
font_name = "Skia"
font(font_name)

#setting the font size
fs = 191

# variable font WGHT axis value
# in Skia's case falls between .48 – 3.2
# WGHT might be changed to whatever axis
wght_value = 200 / 100

# setting the line height percentage
lh_percent = 88

fontSize(fs)
fontVariations(wght = wght_value)
lh = fs * (lh_percent / 100)

word = "TACOFISH"

# vertical position
half = len(word)/2
pos = height()/2 - lh
translate(0, (half * lh))

# using the function
vertext(word, width()/2, pos, lh, "center")

# enjoy