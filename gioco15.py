#Gioco del 15
#Creare la configurazione iniziale
#realizzare una mossa se fattibile
#Inizializzare il gioco avendo come parametri il numero di mosse per scombinarlo
#Le funzioni necessarie sonno tabella, muovi, inizializza gioco, risolto
#Muovi riceve la matrice, che rappresenta una configurazione di gioco qualunque
#riceve d che è una direzione ed x che è il numero di posizioni di quando bisogna spostarsi
#0 destra, 1 sinistra, 2 sopra, 3 sotto
#Inizializza gioco riceve una matrice m e k che indica il numero di mosse a caso
#Muovi restituisce un booleano
#
from random import *

def emptyMatrix(r,c):
    return [[0 for i in range(c)] for j in range(r)]

def stampaMatrice(m):
    for i in range(len(m)):
        print(m[i])

def tabella(): #Crea il gioco, tabella in posizione iniziale
    m = emptyMatrix(4,4)
    for x in range(15):
        m[x//4][x%4] = x + 1 #Passa da una riga all' altra sequenziale con resto
    return m

def risolto(m): #Passano una matrice, restituisce vero se m è lo schema di tabella
    return m == tabella()

def muovi(m,d,x): #Mancante
    rVuota = 0
    cVuota = 0
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0:
                rVuota = i
                cVuota = j
                break
    if d == 0: #Muovi a Destra ->
        if cVuota + x < 4:
            while x > 0:
                m[rVuota][cVuota] = m[rVuota][cVuota+1]
                cVuota += 1
                x -= 1
            m[rVuota][cVuota] = 0
            return True
    if d == 1: #Muovi a Sinistra <-
        if cVuota - x < 0:
            while x > 0:
                m[rVuota][cVuota] = m[rVuota][cVuota-1]
                cVuota -= 1
                x -= 1
            m[rVuota][cVuota] = 0
            return True
    if d == 2: #Muovi in Alto ^
        if rVuota - x < 0:
            while x > 0:
                m[rVuota][cVuota] = m[rVuota-1][cVuota]
                rVuota -= 1
                x -= 1
            m[rVuota][cVuota] = 0
            return True
    if d == 3: #Muovi in Basso _
        if rVuota + x < 4:
            while x > 0:
                m[rVuota][cVuota] = m[rVuota+1][cVuota]
                rVuota += 1
                x -= 1
            m[rVuota][cVuota] = 0
            return True
    return False

def inizializzaGioco(m,k):
    while k > 0:
        d = randint(0,3)
        x = randint(1,3)
        if muovi(m,d,x):
            k -= 1
    return m

tabella = tabella()
tavola = inizializzaGioco(tabella, 21)
stampaMatrice(tavola)

while tabella() != tavola:
    direzione = int(input("Direzione? "))
    passi = int(input("Passi? "))
    muovi(tavola, direzione, passi)
    if tavola == tabella():
        print("Hai vinto!!")
    else:
        stampaMatrice(tavola)
