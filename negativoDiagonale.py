#Solo Diagonale
import cImage as image

img = image.Image("test.gif")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(1,15)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    
        p = img.getPixel(row, row)
       
        newred = 255 - p.getRed()
        newgreen = 255 - p.getGreen()
        newblue = 255 - p.getBlue()
        
        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(row, row, newpixel)

img.draw(win)
win.exitonclick()
