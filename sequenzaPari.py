#03/11/2016

#Data una sequenza di numeri, capiamo se è una sequenza pari
condizione = True #Booleana
k = 0

n = int(input("Quanti numeri vuoi inserire? -> "))

while k<n: #and condizione (altro metodo per uscire dal while
    x=int(input("Inserisci un numero -> "))
    k+=1 #Contatore + 1
    if not x%2 == 0: #Controllo del resto
        condizione = False
        #k=n+1 #Per interrompere il programma k=n+1
        break #Interrompe anche il ciclo
    print("Numero inserito:", x, ", ne mancano ancora", n-k, "da inserire.")

if condizione:
    print("La sequenza contiene solo numeri pari")
else:
    print("La sequenza contiene numeri dispari!")
        
    
