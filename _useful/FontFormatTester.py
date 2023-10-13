for f in installedFonts():
    if f.startswith("."):
        continue
    font(f)
    if fontFilePath().endswith(".ttf"):
        print(f)
