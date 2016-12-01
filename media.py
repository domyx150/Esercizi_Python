print("---- Questo programma serve a calcolare la media dei tuoi voti ----")
print("")
numEsami= int(input("Quanti esami hai sostenuto in totale? -> "))

contatore = 0
somma = 0
votoMin = 0
esami = [0] * numEsami

voto = int(input("Inserisci il primo voto -> "))
contatore = contatore + 1
if voto <= 30 and voto >= 18:
    somma = somma + voto
    votoMin = voto
    votoMax = voto
    esami[0] = voto
    maxEsami = esami[0]
else:
    print("Inserisci un voto valido!")
    contatore = contatore - 1
        
while contatore < numEsami:
    voto = int(input("Inserisci il prossimo voto -> "))
    contatore = contatore + 1
    if voto <= 30 and voto >= 18:
        somma = somma + voto
        esami[contatore-1] = voto
        if votoMin > voto:
            votoMin = voto
        if voto > votoMax:
            votoMax = voto
        for voto in esami:
            if voto > maxEsami:
                maxEsami = voto
    else:
        print("Inserisci un voto valido!")
        contatore = contatore - 1

media = somma/numEsami
countEsami = esami.count(0)
moda = 0
for voto in esami:
    if esami.count(voto) > countEsami:
        countEsami = esami.count(voto)
        moda = voto
##################################################

#Sorting per max 24/11/16
esami.sort()
votoSort = esami[0]
moda2 = esami[0]
freqMax = 1
contatore = 1
for i in range(1,len(esami)):
    if esami[i] == votoSort:
        contatore +=1
    else:
        if contatore > freqMax: #con il >= restituiamo il massimo voto piu' frequente
            freqMax = contatore
            moda2 = votoSort
        votoSort = esami[i]
        contatore = 1
if contatore >= freqMax:
    moda2 = votoSort
    
     
print(votoSort, moda2, freqMax, contatore)

##################################################
        

print("La media è", media)
print("")
print("Il voto massimo è", votoMax)
print("")
if media <= 22:
    print("Impegnati di più! Puoi farcela!")
if media >= 23 and media <= 27:
    print("Non male per essere in questo corso! Fai uso di sostanze per il doping percaso?")
if media >=28 and media < 30:
    print("Rasenti la perfezione! Fantastico!")
if media >= 30:
    print("O stai imbrongliando, o con tutti questi 30 sei un fottuto genio! Bravo!")
print("")
if votoMin <= 22:
    print("Quel", votoMin, "è in Analisi con Punzo, vero?")
print("")
print("")
print("Riprenderemo il programma dopo una breve pausa. (cit.)")
print("")
print("esami: ", esami)
print("maxEsami: ", maxEsami)
print("countEsami: ", countEsami)
print("moda: ", moda)
