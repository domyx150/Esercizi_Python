#Metodi per inizializzare una lista
#create un array di dimensione 10
v=[0]*10
print("V primo", v)
v2=[i for i in range(10)] #Elementi da 0 a 9, solo in python
print("V secondo", v2)
#lista di numeri non primi da 2 a 50
noprimi=[j for i in range(2,50) for j in range(2*i, 50, i)]
#restituisce prima i numeri 4,6,8,10,12..., poi aumenta di 3, 
print("noprimi", noprimi)
#per ottenere i numeri primi
primi=[x for x in range(2,50) if x not in noprimi]
print("primi", primi)
