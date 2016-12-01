#implementare una funzione "generaliste" che crea due liste di interi di uguale dimensione
#prende in ingresso due liste di interi e ne definisce un altra in output
#v3 è generata: se l' indice i che uso per accedere è pari, nell' iesimo elemento di v3 (es. v3[0]) ci finisce la somma degli elementi di v[0] in v1 e v2
#se i è dispari, mettiamo il prodotto degli elementi di v2 che eseguono quell' indice
#es. v1=[1,4,3,8,7] v2=[2,6,5,10,11] , indice 1, somma 4+3+8+7
#i pari -> somma degli elementi di v1 che seguono v1[i]
#i dispari -> prodotto degli elementi di v2 che seguono v2[i]

def generaLista(v1,v2):
    v3=[0]*len(v1)
    for i in range(len(v1)-1):
        if i%2 == 0:
            somma = 0
            for j in range(i+1,len(v1)):
                somma += v1[j]
            v3[i]=somma
        else:
            prodotto = 1
            for j in range(i+1,len(v1)):
                prodotto *= v1[j]
            v3[i]=prodotto
    return v3

v1=[1,4,3,8,7]
v2=[2,6,5,10,11]
v3=generaLista(v1,v2)
print(v3)
