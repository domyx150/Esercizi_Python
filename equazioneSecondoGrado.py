import math
#03/11/2016

#Dato un valore dei coeficenti di un equazione di secondo grado (ax^2+bx+c=0), trova il valore delle x
a = 0

print("Inserisci i coeficenti di ax^2+bx+c=0")

while a == 0a=int(input("Inserisci il coeficente a -> "))
    if a == 0:
        print("Inserisci un numero diverso da 0!")

b=int(input("Inserisci il coeficente b -> "))

c=int(input("Inserisci il coeficente c -> "))

delta = b**2 - 4*a*c

if delta < 0:
    print("Il delta è minore di 0, l' equazione non ha soluzione!")
if delta == 0:
    print("Il delta è uguale a 0, la soluzione è unica!")
    print("La soluzione è", (-b+math.sqrt(delta))/2*a)
if delta > 0:
    print("Il delta è maggiore di 0, le soluzioni sono 2!")
    print("Le soluzioni sono", (-b+math.sqrt(delta))/2*a, "e", (-b-math.sqrt(delta))/2*a)
