import math
#03/11/2016

#Definire se un numero è primo

n = int(input("Inserisci un numero -> "))
primo = True #Condizione per il numero primo
k = 2 #Numero divisibile che incrementa

while k<=math.sqrt(n) and primo: #Per uscire dal while quando il numero è primo #Per ottimizzare, posso già dividere n/2, o ancora meglio con la radice di n
    if n%k == 0:
        primo = False
        print("Il numero non è primo, poichè è stato possibile dividerlo per", k)
    else:
        k+=1

print("Il numero", n, "è un numero primo.")


        
