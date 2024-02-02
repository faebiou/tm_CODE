#drawbot
# script for drawbot extension in robofont
# draws a fitted / interpolating image from a responsive lettering ufo over in two complementary rectangles
# erik@letterror.com / 20231204
# @faebiou forever indebted to @justvanrossum obviously / 20231220
# v2.0 – now with easier-to-change colors and save location! / 20240125

# 2500 / 500

# foreground & background
fg = [1, 0, 1] # magenta
bg = [1, 1, 0] # yellow

# change below for saving directory
saveDir = "/Users/faebiou/Desktop"

fps = 30
seconds = 1

def ip(a, b, f):
    return a + f * (b-a)
    
f = CurrentFont()

vOff = f.info.descender
names = ["narrow-thin", "wide-thin", "narrow-bold", "wide-bold"]

masters = []
for name in names:
    g = f[name].copy()
    g.moveBy((0, -f.info.descender))
    masters.append(g.toMathGlyph())
nt, wt, nb, wb = masters

ntBounds = f["narrow-thin"].getLayer("bounds").bounds
wtBounds = f["wide-thin"].getLayer("bounds").bounds
nbBounds = f["narrow-bold"].getLayer("bounds").bounds
wbBounds = f["wide-bold"].getLayer("bounds").bounds

xMin, yMin, xMax, yMax = ntBounds
narrowX = xMax-xMin
narrowY = yMax-yMin
narrowYMin = yMin
print('narrowYMin', narrowYMin)

xMin, yMin, xMax, yMax = wtBounds
wideX = xMax-xMin
wideY = yMax-yMin
wideYMin = yMin
print('wideYMin', wideYMin)

def interpolate(w, h, weightFactor):
    wantWidth = w
    wantHeight = h
    wantRatio = wantWidth / wantHeight
    wantScale = wantHeight / narrowY

    for n in names:
        assert n in f

    widthFactor = ((wantRatio * narrowY) - narrowX) / (wideX - narrowX)

    w1 = ip(nt, wt, widthFactor)
    w2 = ip(nb, wb, widthFactor)

    return ip(w1, w2, weightFactor), wantScale


duration = 1 / fps
total = seconds * fps
margin = narrowX

def mover(step):
    newPage(1080, 1920)
    frameDuration(duration)
    with savedState():
        t = step / total
        tt = -cos(2 * pi * t) / 2 + 0.5
        weightFactor = tt   
        
        Y = margin + (height() - 2 * margin) * tt
        
        box1 = (width(), Y)
        box2 = (width(), height() - Y)

        fill(*fg)
        rect(0, 0, *box1)
        fill(*bg)
        rect(0, Y, *box2)

        g1, wantScale1 = interpolate(*box1, weightFactor)
        scale(wantScale1)

        with savedState():   
            translate(0,vOff-narrowYMin)
            fill(*bg)
            drawGlyph(g1)

        g2, wantScale2 = interpolate(*box2, (1 - weightFactor))
        scale(wantScale2/wantScale1)
        
        fill(*fg)
        offY = Y / wantScale2
        
        translate(0, offY)
        with savedState():
            translate(0,vOff-narrowYMin)
            drawGlyph(g2)

for frame in range(0, total, 1):
    mover(frame)

        
saveImage(f"{saveDir}/{f.info.familyName}_{total}.gif")