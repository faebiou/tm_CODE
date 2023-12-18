im = ImageObject()

with im:
    # change this to the function of your desire:
    oval(50, 180, 100, 100)
    
center = (width()/2,height()/2)

for deg in range(8):
    rotate(deg * 45, center = center)
    image(im, center)