# defining a function that sets a word vertically
# word is a string, x and y _start are the coordinates
# lineheight is the distance between letters
# alignment can be center, left, or right
def vertext(word, x_start, y_start, line_height, alignment):
   
    # loop through the word
    for letter in range(len(word)):
        # place letters one by one in the correct position
        text(word[letter], (x_start, y_start - (letter * line_height)), align = alignment)

# page size
newPage("A4")

# setting the font
font_name = "Skia"
font(font_name)

# vertical position
pos = 652

#setting the font size
fs = 152

# variable font WGHT axis value
# in Skia's case falls between .48 – 3.2
# WGHT might be changed to whatever axis
wght_value = 226 / 100

# setting the line height percentage
lh_percent = 120

fontSize(fs)
fontVariations(wght = wght_value)
lh = fs * lh_percent / 100

# using the function
vertext("WHAT", width()/2, pos, lh, "center")

# enjoy