#Dati lati del poligono, costruiscilo

import turtle
k=0
wn = turtle.Screen()
poligono = turtle.Turtle()

n=int(input("Inserisci il numero di lati"))
lato = int(input("Inserisci lunghezza del lato"))
angolo=360/n

while n >= k:
    poligono.forward(lato)
    poligono.left(angolo)
    k+=1
    

