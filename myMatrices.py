from random import *

def randArray(numElements, minValue, maxValue):
    """Genera un array casuale con numElements elementi
       nell'intervallo minValue...maxValue """
    a = []
    for i in range(numElements):
        a.append(randint(minValue, maxValue))
    return a


def randMatrix(r,c,minValue=0,maxValue=100):
    """Genera una matrice casuale r x c con elementi
       nell'intervallo minValue...maxValue """
    m = [randArray(c,minValue,maxValue) for i in range(r)]
    return m

def randBoolMatrix(r, c):
    """Genera una matrice casuale r x c con elementi
       Booleani """
    m = []
    for i in range(r):
        v = randArray(c, 0, 1)
        v1 = []
        for j in range(c):
            if v[j] == 0:
                v1.append(False)
            else:
                v1.append(True)
        m.append(v1)
    return m


def emptyMatrix(r,c):
    """Genera una matrice di 0 di dimensione r x c """
    return initMatrix(r,c,0)

def initMatrix(r,c,value=0):
    """Genera una matrice di dimensione r x c con value in tutti gli elementi"""
    return [ [value for i in range(c)] for j in range(r) ]


def printMatrix(m):
    """Stampa in output una matrice allineando opportunamente"""
    #trasformiamo tutto in stringhe e calcoliamo la stringa più lunga
    lMax=0
    ms = []
    for i in range(len(m)):
        riga = []
        for j in range(len(m[i])):
            s = str(m[i][j])
            if len(s) > lMax :
                lMax = len(s)
            riga.append(s)
        ms.append(riga)
    #stampiamo allineando a destra in un campo grande lMax
    for i in range(len(ms)):
        print("|",end="")
        for j in range(len(ms[i])):
            print(ms[i][j].rjust(lMax+1),end="")
        print("|")

def inputMatrix() :
    """Legge riga per riga una matrice di stringhe"""
    m= []
    riga = input()
    while riga != "":
        v = riga.split()
        values = [ v[i] for i in range(len(v))]
        m.append(values)
        riga = input()
    return m

def stringToNumeric (m) :
    """Converte la matrice di stringhe in una matrice numerica"""
    ris = []
    for i in range(len(m)):
        riga = [ eval(m[i][j]) for j in range(len(m[i]))]
        ris.append(riga)
    return ris
            
    
def somma (m1,m2) :
    if len(m1)!= len(m2) or len(m1[0])!= len(m2[0]):
        return None
    m3 = emptyMatrix(len(m1),len(m1[0]));
    for i in range(len(m3)):
        for j in range(len(m3[0])):
            m3[i][j] = m1[i][j] + m2[i][j]
    return m3

def sommaRiga(v1,v2):
    v3 = []
    for i in range(len(v1)):
        v3.append(v1[i]+v2[i])
    return v3
        
def sommaComp (m1,m2) :
    if len(m1)!= len(m2) or len(m1[0])!= len(m2[0]):
        return None
    return [ sommaRiga(m1[i],m2[i]) for i in range(len(m1))]
    
def mult(m1,m2):
    """Calcola il prodotto di m1 ed m2, oppure
       None se le dimensioni non sono compatibili """
    r = len(m1)
    c = len(m2[0])
    if len(m2)!= len(m1[0]):
        return None
    m3=emptyMatrix(r,c)
    for i in range(r):
        for j in range(c):
            for k in range(len(m2)):
                m3[i][j]= m3[i][j]+ m1[i][k]*m2[k][j]
    return m3

def test(r1,c1,c2,minValue=0,maxValue=20):
    m1= randMatrix(r1,c1,minValue,maxValue)
    m2= randMatrix(c1,c2,minValue,maxValue)
    printMatrix(m1)
    print()
    printMatrix(m2)
    print("\nProdotto :")
    m3=mult(m1,m2)
    printMatrix(m3)
    


      
