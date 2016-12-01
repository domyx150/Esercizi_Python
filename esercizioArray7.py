#restituisce in output una lista contenente tutte le sottostringhe palindrome distinte
#di s di lunghezza pari a k

#s = ["abaaa"]
#k = 3


##def trovaSottostringhePalindrome(s,k):
##    l = []
##    j = 0
##    while k >= len(s):
##        k += 1
##        c = k
##        j += 1
##        while j < k and c == 0:
##            j += 1
##            c -= 1
##            if s[j] == s[c]:
##                l.append(s[j])
##    return l

##def trovaSottostringhePalindrome(s,k):
##    l = []
##    j = 0
##    for i in range(len(s)):
##        j += 1
##        while j < k:
##            if s[j:j+k] == s[j:j+k
##                             

def trovaSottostringhePalindrome(s,k):
    l = []
    i = 0
    limite=len(s)-k
    while i <= limite:
        sottostringa = ""
        for j in range(i, i+k):
            sottostringa += s[j]
        if palindroma(sottostringa) and sottostringa not in l:
            l.append(sottostringa)
        i += 1
    return l
        
def palindroma(s):
    return s == s[::-1]
    
    
    
s = "abaaa"
k = 3
l = trovaSottostringhePalindrome(s,k)
print(l)
