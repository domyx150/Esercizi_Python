#Verifica che la lista V è ottenuta concatenando più volte la lista W
#Concatenata True



def texture(v,w): #Restituisce un booleano
    if len(W)>len(V):
        return False
    for i in range(len(V)):
        j = i%(len(W))
        if V[i] != W[j]:
            return False
    return True


V = ["c","i","a","o","c","i","a","o","c","i","a","o","c","i","a"]
W = ["c","i","a","o"]
Z = texture(V,W)
print(Z)
    
                
                
                
            
