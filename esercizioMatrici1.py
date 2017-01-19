#Gestione delle matrici 15/12/16
def sommaMatrici(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]): #Numero di righe della matrice
        return None
    m3 = emptyMatrix(len(m1),len(m1[0]))
    for i in range (len(m3)):
        for j in range (len(m3[0])):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

###_MANCA_EMPTYMATRIX_###

def stampaMatrice(m):
    for i in range(len(m)):
        print(m[i])
       
            
def driangoloSuperiore(m): #Restituisce un array con tutti gli elementi del triangolo superiore inclusa la diagonale principale
    v = []    
    for i in range(len(m)):
        for j in range(i,len(m[0])): #Per evitare diagonale i+1 | da 0 ad i per l' inferiore
            v.append(m[i][j])
    return v

def diagonalePrincipale(m):
    v = []
    for i in range(len(m)):
        v.append(m[i][i])
##    for i in range(len(m)):
##        for j in range(len(m[0])):
##            if i == j:
##                v.append(m[i][j])
    return v

def diagonaleSecondaria(m):
    v = []
    for i in range(len(m)):
        v.append(m[i][len(m[0])-1-i])
    return v

def prodottoMatrici(m1,m2):
    if len(m1[0]) != len(m2): 
        return None
    m3 = emptyMatrix(len(m1),len(m2[0]))
    #Pensiamo a riempire la matrice m3
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            m3[i][j] = 0
            for k in range(len(m2):
                m3[i][j] += m1[i][k] * m2[k][j]
    return m3

###Generare matrici o array che contengono roba
##def emptyMatrix(r,c):
##    v = [2**i for i in range(4)]
##m = [0 for i in range(c)] for j in range(r)]


            
    







    
    
