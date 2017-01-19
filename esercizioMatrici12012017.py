"""
Trovare i punti di sella di una matrice
Punti di sella sono contemporaneamente il minimo della riga i ed il massimo della colonna j
Ottenere coppie di indici della forma i, j che individuano la posizione dei punti di sella. Se non esistono, lista vuota
M[i][j]
"""

def minRiga(m,i):
    numMin = m[i][0]
    for j in range(len(m[i])):
        if m[i][j] < numMin:
            numMin = m[i][j]
    return numMin

def maxCol(m,j):
    numMax = m[0][j]
    for i in range(len(m)):
        if m[i][j] > numMax:
            numMax = m[i][j]
    return numMax

def puntiSella(m):
    l = []
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == minRiga(m,i) and m[i][j] == maxCol(m,j):
                l.append((i,j))
    return l

m = [[4,5,5,9],
     [6,7,6,7],
     [6,8,6,9],
     [5,2,3,3]]

print(puntiSella(m))


