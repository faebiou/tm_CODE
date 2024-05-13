import sys, os
import time
import random as r
from drawBot import *

# returns the name of the file, without its extension
def fName():
    f = os.path.basename(sys.argv[0])
    return os.path.splitext(str(f))[0]

# returns a timestamp like YEAR_MONTH_DAY where the year is only the last two digits
def timestamp():
    ts = time.strftime("%y_%m_%d", time.localtime())
    return ts

# same as timestamp() but with hours and minutes
def timestamp_hour():
    ts = time.strftime("%y_%m_%d_%H_%M", time.localtime())
    return ts

# adds a caption in the corner with the filename and time of running
def info():
    font("Menlo")
    fontSize(6)
    text(fName() + ".py | " + timestamp_hour(), (30, 30))


# adds a caption in the corner with the filename with some extra string
def info_extra(s):
    font("Menlo")
    fontSize(6)
    text(fName() + ".py | " + timestamp_hour() + " | " + s, (30, 30))


# places a grey background of desired lightness
def bg(c):
    fill(c)
    rect(0, 0, width(), height())


# distance formula thanks to Pythagoras
def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# the OG midoval also known as circle()
def midoval(x, y, s):
    oval(x - s / 2, y - s / 2, s, s)


# similar to midoval, but with a rect of course
def midrect(x, y, r):
    rect(x - r / 2, y - r / 2, r, r)


# Just's circle()
def circle(x, y, r):
    oval(x - r, y - r, 2 * r, 2 * r)


# equilateral triangle, sort of
def triangle(x, y, h):
    a = (2 / sqrt(3)) * h
    polygon((x - a / 2, y - h / 2), (x, y + h / 2), (x + a / 2, y - h / 2))


def Vg(x):
    line((x, 0), (x, height()))


def Hg(y):
    line((0, y), (width(), y))


# takes a HEX color and converts it to RGB
def to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")

    r_hex = hex_color[0:2]
    g_hex = hex_color[2:4]
    b_hex = hex_color[4:6]

    r = int(r_hex, 16)
    g = int(g_hex, 16)
    b = int(b_hex, 16)

    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0

    return r_normalized, g_normalized, b_normalized


# takes an RGB color and converts it to HEX
def to_hex(r, g, b):
    r = min(max(r, 0), 1)
    g = min(max(g, 0), 1)
    b = min(max(b, 0), 1)

    r_decimal = int(r * 255)
    g_decimal = int(g * 255)
    b_decimal = int(b * 255)

    r_hex = format(r_decimal, "02x")
    g_hex = format(g_decimal, "02x")
    b_hex = format(b_decimal, "02x")

    hex_color_code = "#" + r_hex + g_hex + b_hex

    return hex_color_code

def insert(sourceText, bothFiles, fontSize, insertWeight):
    newText = FormattedString()
    for word in sourceText:
        newText.append(f"{word} ", font=r.choices(bothFiles, weights=(1, insertWeight), k=1), fontSize=fontSize)
    return newText
    
def insert_multiple(sourceText, allFiles, fontSize, lineHeight, insertWeights):
    newText = FormattedString()
    for word in sourceText:
        newText.append(f"{word} ", font=r.choices(allFiles, weights=(1, *insertWeights), k=1), fontSize=fontSize, lineHeight=lineHeight)
    return newText