"""
Istogramma Grigio ed RGB
v2.1
07/01/2017
Domenico Bruzzese
"""

import cImage as image
import turtle

print("--- Questo programma converte un immagine in bianco e nero e ne crea un istogramma su scala di grigi e modello RGB ---")
print("")
#####_ALTERNATIVA ALLA SCALA AUTOMATICA_#####
##print("Per visualizzare interamente l' istogramma, inserire un livello di scala adeguato. (Consigliato: 6)")
##
##scala = int(input("Inserisci un numero per il rapporto in scala dell' istogramma -> "))
##print("")
print("Procediamo con l' inserimento dell' immagine!")
oldimage = image.Image(input("Inserisci il nome del file nel formato name.xxx -> "))
print("")
print("Il processo è in corso, guarda le altre finestre!")
width = oldimage.getWidth()
height = oldimage.getHeight()

myimagewindow = image.ImageWin("Image Processing",width*3,height*2)
oldimage.draw(myimagewindow)

newim = image.EmptyImage(width,height)
newimR = image.EmptyImage(width,height)
newimG = image.EmptyImage(width,height)
newimB = image.EmptyImage(width,height)


##Porta la turtle in uno stato iniziale in basso a destra
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

numPixel = list(range(256))
numPixelR = list(range(256))
numPixelG = list(range(256))
numPixelB = list(range(256))
numPixelMax = 0
numPixelMaxR = 0
numPixelMaxG = 0
numPixelMaxB = 0

##Controlla tutti i pixel
for col in range(oldimage.getWidth()):
    for row in range(oldimage.getHeight()):
        
        p = oldimage.getPixel(col,row)
        #Livello di grigio
        lGrigio = (p.getRed() + p.getGreen() + p.getBlue()) // 3 #Calcola la media di valore tra i colori per la scala di grigio
        numPixel[lGrigio] += 1 #Incrementa il numero dei pixel di quel colore di 1

        newpixel = image.Pixel(lGrigio, lGrigio, lGrigio)
        newpixelR = image.Pixel(p.getRed(), 0, 0)
        newpixelG = image.Pixel(0, p.getGreen(), 0)
        newpixelB = image.Pixel(0, 0, p.getBlue())

        newim.setPixel(col, row, newpixel)
        newimR.setPixel(col, row, newpixelR)
        newimG.setPixel(col, row, newpixelG)
        newimB.setPixel(col, row, newpixelB)

        #RGB
        lRed = p.getRed() #Calcola la quantità di colore del pixel
        lGreen = p.getGreen()
        lBlue = p.getBlue()
        numPixelR[lRed] += 1 #Incrementa il numero dei pixel di quel colore di 1
        numPixelG[lGreen] += 1
        numPixelB[lBlue] += 1

newim.setPosition(width+1,0) #Affianca l' immagine generata in scala di grigi
newimR.setPosition(0,height+1)
newimG.setPosition(width+1,height+1)
newimB.setPosition(width*2+1,height+1)
newim.draw(myimagewindow)
newimR.draw(myimagewindow)
newimG.draw(myimagewindow)
newimB.draw(myimagewindow)
                        

##Assegnazione Scala
for i in range(255): #Risolve il problema della crescenza dell' indice
    numPixel[i] -= i
    numPixelR[i] -= i
    numPixelG[i] -= i
    numPixelB[i] -= i
numPixelMax = max(numPixel) 
numPixelMaxR = max(numPixelR)
numPixelMaxG = max(numPixelG)
numPixelMaxB = max(numPixelB)
print(numPixelMax)

numPixelMaxS = max(numPixelMax, numPixelMaxR, numPixelMaxG, numPixelMaxB) #Massimo dei massimi

##if numPixelMaxS%480 < 240:
##    scala = numPixelMaxS//480
##else:
##    scala = numPixelMaxS//480 + 1

##scala = 0
##numPixelMaxST = numPixelMaxS
##while numPixelMaxST > 400:
##    scala += 0.1
##    numPixelMaxST = numPixelMaxS - (scala*400)

scala = numPixelMaxS//400
#####################################################################################################################

##Disegna l' Istogramma Grigio
oldNumPixel = 0

isto.fillcolor("grey")
isto.begin_fill()
print("Lista dei pixel Grigi: ")
for i in range(255):
    numPixel[i]= numPixel[i]//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixel[i]- oldNumPixel)
    isto.right(90)
    isto.forward(3)
    isto.left(90)
    oldNumPixel = numPixel[i]
    print("value", i, ":", numPixel[i])
isto.end_fill()
    
##Scritte indicative sugli assi
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMax//scala)
y.write(numPixelMax, True, align="right")
x.write(255, True, align="right")
text.forward(((numPixelMax//scala)//2) +3)
text.write("Istogramma Scala di Grigi, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))
print("")

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Rosso?")

##Porta la turtle in uno stato iniziale in basso a destra
isto.reset()
x.reset()
y.reset()
text.reset()
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

##Disegna l' Istogramma Rosso
oldNumPixel = 0

isto.fillcolor("red")
isto.begin_fill()
print("Lista dei pixel Rossi: ")
for i in range(255):
    numPixelR[i]= numPixelR[i]//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelR[i]- oldNumPixel)
    isto.right(90)
    isto.forward(3)
    isto.left(90)
    oldNumPixel = numPixelR[i]
    print("value", i, ":", numPixelR[i])
isto.end_fill()
    
##Scritte indicative sugli assi
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxR//scala)
y.write(numPixelMaxR, True, align="right")
x.write(255, True, align="right")
text.forward(((numPixelMaxR//scala)//2) +3)
text.write("Istogramma colore Rosso, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))
print("")

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Verde?")

##Porta la turtle in uno stato iniziale in basso a destra
isto.reset()
x.reset()
y.reset()
text.reset()
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

##Disegna l' Istogramma Verde
oldNumPixel = 0

isto.fillcolor("green")
isto.begin_fill()
print("Lista dei pixel Verdi: ")
for i in range(255):
    numPixelG[i]= numPixelG[i]//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelG[i]- oldNumPixel)
    isto.right(90)
    isto.forward(3)
    isto.left(90)
    oldNumPixel = numPixelG[i]
    print("value", i, ":", numPixelG[i])
isto.end_fill()
    
##Scritte indicative sugli assi
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxG//scala)
y.write(numPixelMaxG, True, align="right")
x.write(255, True, align="right")
text.forward(((numPixelMaxG//scala)//2) +3)
text.write("Istogramma colore Verde, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))
print("")

#####################################################################################################################

nIsto = input("Procedere con l' istogramma del colore Blu?")

##Porta la turtle in uno stato iniziale in basso a destra
isto.reset()
x.reset()
y.reset()
text.reset()
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

##Disegna l' Istogramma Blu
oldNumPixel = 0

isto.fillcolor("blue")
isto.begin_fill()
print("Lista dei pixel Blu: ")
for i in range(255):
    numPixelB[i]= numPixelB[i]//scala #Elimina il problema del numero di pixel non impostato a 0 ed imposta la scala
    isto.forward(numPixelB[i]- oldNumPixel)
    isto.right(90)
    isto.forward(3)
    isto.left(90)
    oldNumPixel = numPixelB[i]
    print("value", i, ":", numPixelB[i])
isto.end_fill()
    
##Scritte indicative sugli assi
isto.hideturtle()
x.write(0, True, align="right")
x.forward(768)
y.left(90)
y.forward(numPixelMaxB//scala)
y.write(numPixelMaxB, True, align="right")
x.write(255, True, align="right")
text.forward(((numPixelMaxB//scala)//2) +3)
text.write("Istogramma colore Blu, controlla la Shell per continuare", True, align="center", font=("Arial", 16, "bold"))
print("")

myimagewindow.exitOnClick()
