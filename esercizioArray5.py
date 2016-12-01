#Lista di interi ed intero x, restituisce una nuova lista
#formata dai massimi delle sottolista di a, ottenute considerando
#x elementi consecutivi di a per volta

##def massimi(a,x):
##    maxA = [0]*x
##    for i in range(len(a)):
##        j = i%x
##        if a[i] >= maxA[j]:
##            maxA[j] = a[i]
##    return maxA

def massimi(a,x):
    l = []
    i = 0
    while i < len(a):
        if i+x <= len(a):
            l.append(max_sottolista(a,i,i+x))
        else:
            l.append(max_sottolista(a,i,len(a)))
        i += x
    return l

def max_sottolista(a,i,j):
    massimo = 0
    for k in range(i,j):
        if massimo < a[k]:
            massimo = a[k]
    return massimo

a = [-3,2,3,8,9,10,128,256,10,15]
x = 4
l = massimi(a,x)
print(l)
##l = [8,256,15]
##s1 = [-3,2,3,8]
##s2 = [9,10,128,256]
##s3 = [10,15]

