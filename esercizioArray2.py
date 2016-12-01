#scrivere una funzione rollup prende in ingresso una lista v di interi di dimensioni n con n pari
#restituisce in output una lista w di dimensione n/2 per la quale l' iesimo elemento di w è costruito come segue
#w[i] = v[2*i] + v[2*i + 1]

def rollup(v):
    w=[0]*(len(v)//2)
    for i in range((len(v)//2)-1):
        w[i] = v[2*i] + v[2*i + 1]
    return w

v=[1,5,32,5,8,6]
w=rollup(v)
print(w)

