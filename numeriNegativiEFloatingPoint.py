#08/11/2016
<Per rappresentare i numeri negativi>
    1) Aggiungere un bit per definire positivita' e negativita'
    2) Complemento a due:
        si utilizza una rappresentazione del numero diversa, rappresentando il numero x come 2^b + x
        con b indichiamo i bit a disposizione, con x il numero da rappresentare
        es il numero -3 con 4 bit, abbiamo 2^4-3
        nel primo caso, 0011 viene invertito, indicando 1100 e sommando 1, si ottiene 1101, che e' il numero -3 in complemento a 2
        i numeri in complemento a 2 iniziano sempre con 1 se negativi, 0 se positivi
        il numero ottenuto in decimale e' 13 (2^4-3=13)
        se sommiamo 3(0011) a questo -3(1101) otteniamo 0((1)0000). Il superamento viene inteso come 0, non avendo un numero di bit b+1 a disposizione

        nel 2^4 + 3, otteniamo 16(10000) + 3(11), quindi +3((1)0011)
        queste 16 combinazioni nei soli numeri positivi danno i numeri da 0 a 15, con i negativi il massimo a +7 ed il minimo negativo a -8
        il numero 1111 per capire in decimale di inverte e si somma 1, quindi 0000 + 1 = 1, quindi -1
        il numero 1001, invertito 0110 + 1 = 0111 = 7, quindi -7
        il numero 1010, invertito 0101 + 1 = 0110 = 6, quindi -6
        il numero 1011, invertito 0100 + 1 = 0101 = 5, quindi -5
        il numero (-8)1000, invertito 0111 + 1 = 1000 = 8, quindi -8, il minimo
        -8+2 è 1000 + 0010 = 1010, quindi invertito 0101 + 1 = 0110 =

<Floating Point>
    Per la rappresentazione dei numeri con la virgola
    es il numero 3.1415
    si cercano di distinguere le cifre significative(1415)
    usiamo un certo numero di bit per la mantissa (cifre significative, la parte intera) ed un certo numero di bit per l' esponente
    quindi 31415 * 10^-4, 0.31415 sarebbe 31415 * 10^-5

    <Test>
    8 bit, mantissa 5 bit ed esponente 3 bit
    in 8 bit abbiamo da 0 a 255 interi non negativi, da -128 a 127 per i negativi e positivi interi
    in questo caso, la mantissa può andare da -16 a +15, l' esponente da -4 a +3
    il più grande è 15 + 10^3 (15'000)
    il più piccolo è 1*10^-4 (0.00001)

    Rappresentiamo numeri grandi e piccoli, ma non tutti quelli disponibili (es non posso rappresentare 14569)
    Rappresentiamo 0,1,2,3,...,15, senza poter rappresentare il 16. Il successivo a 15 è 20, possiamo rappresentarlo come 2*10^1 con la coppia (2,1)
    Serve quindi se non necessito di variazioni piccole

    Float usa 32 bit
    Double usa 64 bit
