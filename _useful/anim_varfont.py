frameNumber = 6
for frame in range(frameNumber):
    
    newPage(1080, 1920)
    frameDuration(1/30)
    fontSize(340)
    font("Skia")
    
    # setting a white BG
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    
    # grabbing the WGHT values for Skia
    min_wght = 0.4799
    max_wght = 3.1999        
    wght_var = remap(frame, 0, frameNumber, min_wght, max_wght)

    # grabbing the WDTH values for Skia
    min_wdth = 0.6199
    max_wdth = 1.3
    wdth_var = remap(frame, 0, frameNumber, min_wdth, max_wdth)

    fontVariations(wght = wght_var, wdth = wdth_var)

    text("SUP", ((width()/2, height()/2)), align = "center")
    
for frame in range(frameNumber):
    
    newPage(1080, 1920)
    frameDuration(1/30)
    fontSize(340)
    font("Skia")
    
    # setting a white BG
    fill(1)
    rect(0, 0, width(), height())
    fill(0)
    
    # grabbing the WGHT values for Skia
    min_wght = 0.4799
    max_wght = 3.1999        
    wght_var = remap(frame, 0, frameNumber, min_wght, max_wght)

    # grabbing the WDTH values for Skia
    min_wdth = 0.6199
    max_wdth = 1.3
    wdth_var = remap(frame, 0, frameNumber, min_wdth, max_wdth)

    fontVariations(wght = wght_var, wdth = wdth_var)

    text("SUP", ((width()/2, height()/2)), align = "center")
    
print(listFontVariations())
saveImage("test.gif")






