#03/11/2016

#Determinare il perimetro del triangolo avendo le misure dei dati in input

a = int(input("Inserisci il primo lato -> "))
b = int(input("Inserisci il secondo lato -> "))
c = int(input("Inserisci il terzo lato -> "))

print(".")

if a==b and b==c:
    print("Il triangolo è equilatero!")
elif a==b or a==c or b==c:
    print("Il triangolo è isoscele!")
else:
    print("Il triangolo è scaleno!")

print(".")
print("Il perimetro è ", a+b+c)
