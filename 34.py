# lists are arbitrary lengths
# tuples are short, immutable list !

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1)]

colors.append((0, 1, 1))

words = ["hello", "type", "and", "media", "how", "are", "you"]

# for c in colors:
#     fill(*c)
#     rect(0, 0, 300, 100)
#     translate(0, 100)

for frame in range(10):
    shuffle(words)
    newPage(1080, 1920)
    frameDuration(1 / 5)
    for i in range(len(words)):
        font("ComicSansMS")
        fontSize(180)
        h = height() / len(words)
        bg = choice(colors)
        fill(*bg)
        rect(0, 0, width(), h)

        fg = choice(colors)
        if fg != bg:
            fill(*fg)
        else:
            fg = choice(colors)
        fill(*fg)

        text(words[i], (0, 0))

        translate(0, h)

saveImage("_exp/34.gif")
