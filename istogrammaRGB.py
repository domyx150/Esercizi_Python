#Domenico Bruzzese

import cImage as image
import turtle

print("--- Questo programma converte un immagine in bianco e nero e ne crea un istogramma su scala di grigi e modello RGB ---")
print("")
print("Per visualizzare interamente l' istogramma, inserire un livello di scala adeguato. (Consigliato: 6)")

scala = int(input("Inserisci un numero per il rapporto in scala dell' istogramma -> "))
print("")
print("Procediamo con l' inserimento dell' immagine!")
oldimage = image.Image(input("Inserisci il nome del file nel formato name.xxx -> "))
print("")
print("Il processo è in corso, guarda le altre finestre!")
width = oldimage.getWidth()
height = oldimage.getHeight()

myimagewindow = image.ImageWin("Image Processing",width*2,height)
oldimage.draw(myimagewindow)

newim = image.EmptyImage(width,height)

def inizializzaTurtle(isto,x,y):
    isto = turtle.Turtle()
    x = turtle.Turtle()
    y = turtle.Turtle()
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.left(90)
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
numPixelR = list(range(255))
numPixelG = list(range(255))
numPixelB = list(range(255))
isto = turtle.Turtle()
x = turtle.Turtle()
y = turtle.Turtle()
    
inizializzaTurtle(isto,x,y)

##Controlla tutti i pixel
for col in range(oldimage.getWidth()):
    for row in range(oldimage.getHeight()):
        
        p = oldimage.getPixel(col,row)
        #Livello di grigio
        lGrigio = (p.getRed() + p.getGreen() + p.getBlue()) // 3 #Calcola la media di valore tra i colori per la scala di grigio
        numPixel[lGrigio] += 1 #Incrementa il numero dei pixel di quel colore di 1

        newpixel = image.Pixel(lGrigio, lGrigio, lGrigio)

        newim.setPixel(col, row, newpixel)

        #RGB
        lRed = p.getRed() #Calcola la quantità di colore del pixel
        lGreen = p.getGreen()
        lBlue = p.getBlue()
        numPixelR[lRed] += 1 #Incrementa il numero dei pixel di quel colore di 1
        numPixelG[lGreen] += 1
        numPixelB[lBlue] += 1


newim.setPosition(width+1,0) #Affianca l' immagine generata in scala di grigi
newim.draw(myimagewindow)        

#####################################################################################################################

##Disegna l' Istogramma Grigio
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
    

##Scritte indicative sugli assi
numPixelMaxPrint = numPixelMax*scala #Risolve il problema della scala in stampa
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMax)
y.write(numPixelMaxPrint, True, align="right")
x.write(255, True, align="right")
text.forward((numPixelMax//2)+3)
text.write("Istogramma Scala di Grigi, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))
print("Lista dei pixel Grigi: ", numPixel)

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Rosso?")

##Porta la turtle in uno stato iniziale in basso a destra
inizializzaTurtle()

##Disegna l' Istogramma Rosso
numPixelMaxR=0
for i in range(255):
    numPixelR[i]=(numPixelR[i]-i)//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelR[i])
    isto.right(90)
    isto.forward(3)
    isto.right(90)
    isto.forward(numPixelR[i])
    isto.left(180)
    if numPixelR[i] > numPixelMaxR:
        numPixelMaxR = numPixelR[i]
    

##Scritte indicative sugli assi
numPixelMaxRPrint = numPixelMaxR*scala #Risolve il problema della scala in stampa
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxR)
y.write(numPixelMaxRPrint, True, align="right")
x.write(255, True, align="right")
text.forward((numPixelMaxR//2)+3)
text.write("Istogramma colore Rosso, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))

print("Lista dei pixel Rossi: ", numPixelR)

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Verde?")

##Porta la turtle in uno stato iniziale in basso a destra
inizializzaTurtle()

##Disegna l' Istogramma Verde
numPixelMaxG=0
for i in range(255):
    numPixelG[i]=(numPixelG[i]-i)//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelG[i])
    isto.right(90)
    isto.forward(3)
    isto.right(90)
    isto.forward(numPixelG[i])
    isto.left(180)
    if numPixelG[i] > numPixelMaxG:
        numPixelMaxG = numPixelG[i]
    

##Scritte indicative sugli assi
numPixelMaxGPrint = numPixelMaxG*scala #Risolve il problema della scala in stampa
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxG)
y.write(numPixelMaxGPrint, True, align="right")
x.write(255, True, align="right")
text.forward((numPixelMaxG//2)+3)
text.write("Istogramma colore Verde, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))

print("Lista dei pixel Verdi: ", numPixelG)

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Blu?")

##Porta la turtle in uno stato iniziale in basso a destra
inizializzaTurtle()

##Disegna l' Istogramma Blu
numPixelMaxB=0
for i in range(255):
    numPixelB[i]=(numPixelB[i]-i)//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelB[i])
    isto.right(90)
    isto.forward(3)
    isto.right(90)
    isto.forward(numPixelB[i])
    isto.left(180)
    if numPixelB[i] > numPixelMaxB:
        numPixelMaxB = numPixelB[i]
    

##Scritte indicative sugli assi
numPixelMaxBPrint = numPixelMaxB*scala #Risolve il problema della scala in stampa
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxB)
y.write(numPixelMaxBPrint, True, align="right")
x.write(255, True, align="right")
text.forward((numPixelMaxB//2)+3)
text.write("Istogramma colore Blue, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))

print("Lista dei pixel Blu: ", numPixelB)




myimagewindow.exitOnClick()


