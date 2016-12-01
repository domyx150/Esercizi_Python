#Due stringhe s1,s2, sono a distanza1 se differiscono al più per un carattere
#output: booleano


##def distanza1(s1,s2):
##    if len(s1) == len(s2):
##        return True
##    i = 0
##    k = 0
##    test = 0
##    while i < len(s1) and k < len(s2):
##        if not s1[i] == s2[k]:
##            test += 1
##            k -= 1
##        i += 1
##        k += 1
##    if test >= 2:
##        return False
##    return True

def distanza1(s1,s2):
    m = len(s1)
    n = len(s2)
    if abs(n-m) > 1:
        return False
    i = 0
    j = 0
    cont = 0
    while i < m and j < n:
        if s1[i] != s2[j]:
            if cont == 1:
                return False
            if n > m:
                i += 1
            elif m > n:
                j += 1
            else: #n = m
                i += 1
                j += 1
            cont += 1
        else:
            i += 1
            j += 1
    if i < m or j < n:
        cont += 1
    if cont <= 1:
        return True
    else:
        return False
    
            
s1 = "abcee"
s2 = "abcd"
l = distanza1(s1,s2)
print(l)
