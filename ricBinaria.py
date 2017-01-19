def ricBinaria(v, x):
    inizio = 0
    fine = len(v) - 1
    while inizio <= fine:
        print("x")
        med = (inizio + fine) // 2
        if v[med] == x:
            return med
        if v[med] > x:
            fine = med - 1
        else:
            inizio = med + 1
    return -1

#Versione alternativa      
def ricBinaria2(v, x, inizio, fine):
    print("x")
    if inizio > fine:
        return -1
    med = (inizio + fine) // 2
    if v[med] == x:
        return med
    if v[med] > x:
        return ricBinaria2(v, x, inizio, med-1)
    else:
        return ricBinaria2(v, x, med+1, fine)
    return -1

#Verzione per potenza di 2
#Assumiamo il n elementi una potenza di 2
##_INCOMPLETO_##
##def ricBinariaPotenza(v, x):
##    inizio = 0
##    fine = len(v) - 1
##    while inizio <= fine:
##        med = (inizio + fine) // 2
##        if v[med] == x:
##            return med
##        if v[med] > x:
##            fine = med - 1
##        else:
##            inizio = med + 1
##    return -1
##_INCOMPLETO_##

v = [1,5,6,11,13,16,18,24,30,36,44,49,62,123,157,255]
x = int(input(""))
l = ricBinaria(v, x)

print(l)
      
