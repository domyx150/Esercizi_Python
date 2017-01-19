"""
traccia 20160225 v3
verifica_matrice riceve interi M di dimensioni nxn e due indici ir jc compresi tra o e n-1
e restituisce true se e solo se, per ogni elemento x presente nella riga ir, m contiene almeno due elementi
uguali ad x al di fuori sia della riga ir che della colonna jc
"""

def verifica_matrice(m,ir,jc):
    """ Mio programma
    somma = 0
    for i in range(len(m)):
        somma = 0
        for j in range(len(m)):
            if not i == ir or j == jc:
                if m[ir][jc] == m[i][j]:
                    somma += 1
                    if somma == 2:
                        return True
    """
    somma = 0
    for x in m[ir]: #Oppure for j in range(len(m)):\x = m[ir][k]
        
        cont_x = 0
        for i in range(len(m)):
            if i != ir:
                for j in range(len(m)):
                    if j != jc:
                        if m[i][j] == x:
                            cont_x += 1

        if cont_x < 2:
            return False
    return True
            

m = [[8,0,3,-9,3],
     [2,3,6,3,-1],
     [1,2,5,7,-1],
     [6,9,2,5,3],
     [3,2,4,-1,6]]

if verifica_matrice(m,1,2):
    print("ok")
else:
    print("no")
                    
                    
                    
                
