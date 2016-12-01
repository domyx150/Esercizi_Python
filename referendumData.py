import math
#03/11/2016
#Il comune di rende vuole capire se qualcuno può votare o no per il referendum del 4/12/2016, condizione quindi età >= 18 anni
print("Il tipo di data è inteso come GG/MM/AAAA")

g = int(input("Inserisci il giorno di nascita -> "))
m = int(input("Inserisci il mese di nascita -> "))
a = int(input("Inserisci l' anno di nascita -> "))

gV = 4
mV = 12
aV = 2016

a = a+18 #Sommo 18 anni all' età del tizio

if a < aV:
    print("Il soggetto può votare")
elif a == aV:
    if m < mV:
        print("Il soggetto può votare 2")
    elif m == mV and g <= gV:
        print("Il soggetto può votare 3")
    else:
        print("Non puoi votare! 3")
else:
    print("Non puoi votare!")
    
    
        
