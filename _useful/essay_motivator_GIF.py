import datetime

now = datetime.datetime.now()
deadline = datetime.datetime(2024, 1, 15)
countdown = deadline - now
panik = round(countdown.days*24 + countdown.seconds/3600, 2)

goal = 3000 # word count requirement

f = open("/Users/faebiou/Library/Mobile Documents/27N4MQEA55~pro~writer/Documents/TM_2324_iA/REVIVAL/LESSONS.md") # path to your text file – use txt, rtf, or md; could work with doc or pages but ¯\_(ツ)_/¯

encourage = ["Essays are like pizza – even when they're messy, they're still satisfying.\nKeep tossing those words onto the page!", "Writing an essay is like a duel with a blank page.\nSpoiler: You're the hero. Keep slaying those paragraphs like a literary ninja.", "Your brain's a party, and the essay is the dance floor.\nLet the words boogie down onto the paper!", "Procrastination is an art form, and you're a master.\nTurn those last-minute ideas into a masterpiece. Time to dazzle the essay gods!", "Your essay is a dramatic soap opera – full of twists, turns\n, and unexpected plot twists. Make it a page-turner!", "Perfectionism is so last season. Your first draft is like fashion's hottest trend – unique, a bit messy, and bound to make a statement. Werk it, writer!", "Your essay is a superhero origin story.\nUnleash your writing superpowers and conquer that blank page!", "Writing is your workout, and each sentence is a rep.\nSculpt that masterpiece – no sweating involved!", "If your essay were a meme, it'd break the internet.\nEmbrace the potential viral greatness of your words.", "If writing an essay were an Olympic sport, you'd be a gold medalist. Flawless mental gymnastics – now go for that perfect dismount: conclusion, here you come!"]




txt = f.read()
wordCount = len(txt.split())

for i in range(10):

    newPage(2000, 500)
    fill(1)
    rect(0, 0, width(), height())
    frameDuration(.5)
    
    marge = 60
    boxH = 270

    linearGradient(
        (marge, 0),
        (width()-marge*2, 0),
        [(1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)],
        [ 0,        .25,       .5,         .75,       1]
        )

    progress = (i + 1)/10
    boxW = remap(progress, 0, 1, 0, width() - marge * 5.5)

    rect(marge, height() / 2 - marge * 1.5, boxW, boxH)

    msg = "%s%%" % round(progress * 100 , 1)
    words = "%s words of " % round(progress * goal) + str(goal) + "\n%s hours left" % panik

    fill(0)
    font("Menlo")
    fontSize(72)
    text(msg, (1773, height() / 2 - marge * 1.5))
    fontSize(30)
    textBox(encourage[i], (marge, marge, 1450, marge + 10))
    textBox(words, (500, marge, 1450, marge + 10), align = "right")

saveImage("essay_motivator.mp4")
