#in: lista di interi v
#out: booleano -> true valori alternati pari/dispari, false altrimenti

def alternati(v):
    for i in range(len(v)-1):
        if v[i]%2 == 0:
            if not v[i+1]%2 == 0:
                alt = True
            else:
                alt = False
                break

    return alt

v=[6,19,18,29,36,47,52]
print(alternati(v))
