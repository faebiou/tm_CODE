steps = 100

pos = { (random() * width(), random() * height()) for i in range(steps) }

fill(None)
stroke(0)

polygon(*pos)