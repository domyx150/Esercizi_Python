#03/11/2016
#Conversione di un numero decimale in esadecimale, >= di 0

risultato = ""
r = 0

n = int(input("Inserisci il numero in base decimale da convertire -> "))
while n > 0:

    if n == 0: #Il numero 0 nei due sistemi è uguale
        risultato += str(n) #Converte un intero a stringa con appeso
        print("Il risultato è", risultato)
    elif 1<=n<=9:
        risultato = str(n) + risultato
        print("Il risultato è", risultato)
    
    r = int(n%16)
    n = (n-r)/16
    resto = str(r)
        
    if r == 10:
        resto = "A"
    if r == 11:
        resto = "B"
    if r == 12:
        resto = "C"
    if r == 13:
        resto = "D"
    if r == 14:
        resto = "E"
    if r == 15:
        resto = "F"

    risultato = resto + risultato
    
print("Risultato 2", risultato)
    
            
     




