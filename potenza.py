#Calcola la potenza di un numero
#Consideriamo potenze intere

contatore = 0
risultato = 0
n = -1
potenza = -1


while n <= 0:
    n = int(input("Inserisci il numero di base -> "))
    if n <= 0:
        print("Inserisci un numero maggiore di 0!")

while potenza < 0:
    potenza = int(input("Inserisci la potenza per cui elevare la base -> "))
    if potenza < 0:
        print("Inserisci un numero maggiore di 0!")

risultato = n

while contatore < potenza - 1:
    risultato = risultato*n
    contatore = contatore + 1

print("Il risultato è", risultato)

#___ COMMENTI AULA ____

#Calcoliamo a^b
#Input: due interi a,b
#Pre: a>0;b>=0
#Output: a^b

#a=int(input("Inserisci la base: ")
#b=int(input("Inserisci espontente: ")

#...

#k = 0

#All' iterazione k, prodotto contiene la produttoria A^k
#prodotto = 1
