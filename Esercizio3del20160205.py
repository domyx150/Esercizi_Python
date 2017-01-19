"""
Traccia 20160205 v3 Esercizio 3
Matrice M nxn, numero di messaggi inviati da utente x ad utente y
In ogni posizione un intero di messaggi inviati
La matrice M non è simmetrica
Amici se hanno scambiato almeno un messaggio
A distanza 2 se non sono amici ma esiste un terzo utente z amico di x ed y
L' utente non può essere amico di se stesso. in i,i sulla matrice m è 0, diagonale principale 0
per ogni coppia di utenti amici si registra l' argomento principale nella matrice T
T è simmetrica di dimensioni nxn (Non è simmetrica in esercizio)
Stringa vuota in coppie di utenti non amici
"""

### Funzioni di supporto ###

def media_amici(m):
    media = 0
    sommaAmici = 0
    for i in range(len(m)):
        amici_i = 0
        for j in range(len(m)):
            if m[i][j] > 0 or m[j][i] > 0:
                amici_i += 1
        sommaAmici += amici_i
    media = sommaAmici / len(m)
    return media
        
### Funzioni dell' esercizio ###

def utenti_popolari(m): #L' output è una lista
    lista_utenti_popolari = []
    media = media_amici(m)
    for i in range(len(m)):
        amici_i = 0
        for j in range(len(m)):
            if m[i][j] > 0 or m[j][i] > 0:
                amici_i += 1
        if amici_i > media:
            lista_utenti_popolari.append(i)
    return lista_utenti_popolari

def distanza_due(m,x): #riceve matrice e codice utente x
    utenti_distanza_due = []
    amici_x = []
    nemici_x = []
    for j in range(len(m)):
        if m[x][j] > 0 or m[j][x] > 0:
            amici_x.append(j)
        elif x != j:
            nemici_x.append(j)
            
    for i in range(len(nemici_x)):
        utente_i = nemici_x[i]
        for j in range(len(amici_x)):
            utente_j = amici_x[j] #Utente Z che fa da collegamento
            if m[utente_i][utente_j] > 0 or m[utente_j][utente_i] > 0:
                utenti_distanza_due.append((utente_i))
                break #Se collegati da altri amici inseriremmo duplicati
            
    return utenti_distanza_due

def interessati_argomento(m,t,a,k): #Restituisce lista di utenti che hanno scambiato almeno k messaggi con un altro utente sull' argomento a
    lista_interessati_argomento = []
    
    for i in range(len(m)):
        somma_messaggi = 0
        
        for j in range(len(m)):
            
            if t[i][j] == a:
                somma_messaggi += m[i][j]

            if t[j][i] == a:
                somma_messaggi += m[j][i]

            if somma_messaggi >= k:
                lista_interessati_argomento.append(i)
                #j viene considerato dopo, non si inserisce per evitare duplicati
                break
    return lista_interessati_argomento
            
def main():
    m = [[0,0,8,0,0,0,],
         [0,0,0,0,0,0,],
         [0,5,0,0,0,0,],
         [0,0,9,0,4,0,],
         [0,0,0,0,0,0,],
         [0,9,0,7,0,0,]]
    t = [["","","calcio","","",""],
         ["","","","","",""],
         ["","cinema","","","",""],
         ["","","cinema","","calcio",""],
         ["","","","","",""],
         ["","politica","","cinema","",""],]
    a = 'cinema'
    k = 7
    print(utenti_popolari(m))
    print(distanza_due(m,2))
    print(interessati_argomento(m,t,a,k))

main()






    
