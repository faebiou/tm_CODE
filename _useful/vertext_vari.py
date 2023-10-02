def vertext(word, x_start, y_start, line_height, alignment):
    for letter in range(len(word)):
        text(word[letter], (x_start, y_start - (letter * line_height)), align = alignment)

pos = 1422
fs = 312

lh_percent = 120

lh = fs * lh_percent / 100

total_frames = 30
total_duration = 1

def anim(direction):
    for frame in range(total_frames):
        
        newPage(1080, 1920)
        
        fill(1)
        rect(0, 0, width(), height())
        fill(0)
        
        frameDuration(total_duration/total_frames)

        font_name = "Skia"
        font(font_name)
        fontSize(fs)

        # change if no WGHT axis is available
        minVal = listFontVariations(font_name)['wght']['minValue']
        maxVal = listFontVariations(font_name)['wght']['maxValue']

        x = direction * remap(frame, 0, total_frames, minVal, maxVal)
        
        if direction >= 0:
            fontVariations(wght = minVal + x)
        else:
            fontVariations(wght = maxVal + x)
            
        vertext("WHAT", width()/2, pos, lh, "center")
        
anim(1)
anim(-1)

saveImage("test.gif")

# enjoy