import os
import fun as f

files = []
extension = ".png"
subfolder = ""

if len(subfolder) > 0:
    for listedFile in os.listdir(subfolder):
        if listedFile.endswith(extension):
            files.append(listedFile)
else:
    for listedFile in os.listdir():
        if listedFile.endswith(extension):
            files.append(listedFile)


for file in range(len(files)):
    newPage()
    f.bg(1)
    currPath = subfolder + files[file]
    img = ImageObject(currPath)
    img_size = img.size()
    image(img, (width() / 2 - img_size[0] / 2, height() / 2 + img_size[1] / 2))
    fill(0)
    fontSize(10)
    f.info_extra(files[file])

saveImage(f.fName() + ".gif")
