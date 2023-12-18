#  imports
import sys
sys.path.append("..")
from helper_functions import *
# --------------------------
#  settings
w, h = 2000, 2000
steps = 50
f_name = 'ZurielThunder-Thunder'
axes = ['THDR', 'THDR'] 
# --------
axis1_min = listFontVariations(f_name)[axes[0]]['minValue']
axis1_def = listFontVariations(f_name)[axes[0]]['defaultValue']
axis1_max = listFontVariations(f_name)[axes[0]]['maxValue']
axis2_min = listFontVariations(f_name)[axes[1]]['minValue']
axis2_def = listFontVariations(f_name)[axes[1]]['defaultValue']
axis2_max = listFontVariations(f_name)[axes[1]]['maxValue']
def_x = map_val(axis1_def, axis1_min, axis1_max, 0, w)
def_y = map_val(axis2_def, axis2_min, axis2_max, 0, h)
# --------------------------
#  functions 
def a_page():
    newPage(w,h)
    fill(.8)
    font(f_name)
    lineHeight(2)
    fontSize(h/8)
    rect(0, 0, w, h)
    var_values = { axes[0] : axis1_min, axes[1] : axis2_min }
    fontVariations( **var_values )
# --------------------------
#  Drawings
for a in range(steps):
    a_page()
    angle = 2 * pi / steps * a
    x = .5 + cos(angle) * .5
    y = .5 + sin(angle) * .5
    fill(0, 1)
    var_values = { axes[0] : ip(axis1_min, axis1_max, x), axes[1] : ip(axis2_min, axis2_max, y) }
    fontVariations( **var_values )
    overflow = textBox('''N
A
Z
G
U
L''',
       (w/4, h/4, w/2, h/2), align="center")
# a text box returns text overflow
# text that did not make it into the box
    print(overflow)
    saveImage('yo.gif')