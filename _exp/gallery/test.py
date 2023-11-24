import glob
import random as r
from dominate import document
from dominate.tags import *

photos = glob.glob('selection/*.gif')
r.shuffle(photos)

with document(title='MOVING IMAGES') as doc:
    for path in photos:
        img(src=path)

with doc.head:
    link(rel='stylesheet', href='style.css')
    script(type='text/javascript', src='script.js')

with open('gallery.html', 'w') as f:
    f.write(doc.render())