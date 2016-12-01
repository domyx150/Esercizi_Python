import cImage as image
import turtle

print("--- Questo programma converte un immagine in bianco e nero e ne crea un istogramma ---")
print(".")
print("Per visualizzare interamente l' istogramma, inserire un livello di scala adeguato. (Consigliato: 6)")

scala = int(input("Inserisci un numero per il rapporto in scala dell' istogramma -> "))
print(".")
print("Procediamo con l' inserimento dell' immagine!")
oldimage = image.Image(input("Inserisci il nome del file nel formato name.xxx -> "))
print(".")
print("Il processo è in corso, guarda le altre finestre!")
width = oldimage.getWidth()
height = oldimage.getHeight()

myimagewindow = image.ImageWin("Image Processing",width*2,height)
oldimage.draw(myimagewindow)

newim = image.EmptyImage(width,height)

##Porta la turtle in uno stato iniziale in basso a destra
isto = turtle.Turtle()
x = turtle.Turtle()
y = turtle.Turtle()
isto.penup()           
isto.speed(0)
isto.setx(-384)
isto.sety(-256)
isto.pendown()
x.penup()           
x.speed(100)
x.setx(-384)
x.sety(-256)
x.pendown()
y.penup()           
y.speed(100)
y.setx(-384)
y.sety(-256)
y.pendown()
isto.left(90)

numPixel = list(range(255))


##Controlla tutti i pixel
for col in range(oldimage.getWidth()):
    for row in range(oldimage.getHeight()):
        
        p = oldimage.getPixel(col,row)
        lGrigio = (p.getRed() + p.getGreen() + p.getBlue()) // 3 #Calcola la media di valore tra i colori per la scala di grigio
        numPixel[lGrigio] += 1 #Incrementa il numero dei pixel di quel colore di 1

        newpixel = image.Pixel(lGrigio, lGrigio, lGrigio)

        newim.setPixel(col, row, newpixel)

newim.setPosition(width+1,0) #Affianca l' immagine generata in scala di grigi
newim.draw(myimagewindow)        


##Disegna l' Istogramma
numPixelMax=0
for i in range(255):
    numPixel[i]=(numPixel[i]-i)//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixel[i])
    isto.right(90)
    isto.forward(3)
    isto.right(90)
    isto.forward(numPixel[i])
    isto.left(180)
    if numPixel[i] > numPixelMax:
        numPixelMax = numPixel[i]
    
    print(numPixel[i])

##Scritte indicative sugli assi
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMax)
y.write(numPixelMax, True, align="right")
x.write(256, True, align="right")



myimagewindow.exitOnClick()
