import time as t

import sys, os

from drawBot import *


def fName():
    f =  os.path.basename(sys.argv[0])
    return os.path.splitext(str(f))[0]

def timestamp():
    Y = str(t.localtime()[0] - 2000)
    M = str(t.localtime()[1])
    D = str(t.localtime()[2])
    H = str(t.localtime()[3])
    M = str(t.localtime()[4])
    S = str(t.localtime()[5])
    return "__" + Y + "_" + M + "_" + D + "__" + H + "_" + M + "_" + S


def bg(c):
    print("hellloooooo")
    fill(c)
    rect(0, 0, width(), height())


def randcolor(c):
    actual = colors[int(random.uniform(0, len(c)))]
    return hex_to_rgb(actual)


def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def midoval(x, y, s):
    oval(x - s / 2, y - s / 2, s, s)


def hex_to_rgb(hex_color):
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


def rgb_to_hex(r, g, b):
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
