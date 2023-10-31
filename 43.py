import fun as f

center = width() / 2, height() / 2

f.bg(0.2)

fill(0.19)
font("Menlo-Bold")
fontSize(300)
text("FAST", (150, 750))
with savedState():
    rotate(-60)
    text("CHEAP", (-633, 270))
with savedState():
    rotate(60)
    text("GOOD", (322, -670))

fill(None)
stroke(0)

f.midoval(width() / 2, height() / 2, 770)

fill(1, 0, 0)

d = 20
pos1 = 500, 885
pos2 = 167, 308
pos3 = 833, 308

line(pos1, pos2)
line(pos2, pos3)
line(pos3, pos1)

pos = 504, 544

line(pos, pos1)
line(pos, pos2)
line(pos, pos3)

fill(1, 0, 0)
f.midoval(*pos1, d)
fill(1, 1, 0)
f.midoval(*pos2, d)
fill(0, 1, 1)
f.midoval(*pos3, d)

fill(1)
f.midoval(*pos, 40)

FAST = 1 - f.dist(*pos, *pos1) / 666
CHEAP = 1 - f.dist(*pos, *pos2) / 666
GOOD = 1 - f.dist(*pos, *pos3) / 666

FAST_factor = 1
CHEAP_factor = 1
GOOD_factor = 1

print(FAST)
print(CHEAP)
print(GOOD)
print()
print(FAST * FAST_factor)
print(CHEAP * CHEAP_factor)
print(GOOD * GOOD_factor)

overall = FAST * FAST_factor * CHEAP * CHEAP_factor * GOOD * GOOD_factor
print()
print(overall)

fill(0)
stroke(None)
font("Menlo")
fontSize(10)

y = 42
fill(1, 0, 0)
rect(30, y, 40, FAST * 170)
text("FAST", (30, y - 16))
fill(1, 1, 0)
rect(80, y, 40, CHEAP * 170)
text("CHEAP", (80, y - 16))
fill(0, 1, 1)
rect(130, y, 40, GOOD * 170)
text("GOOD", (130, y - 16))
