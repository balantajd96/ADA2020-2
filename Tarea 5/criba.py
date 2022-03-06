MAX=32000
esPrimo=None
primos=None
divs=None

def sieve_opt():
    global esPrimo, primos, divs

    esPrimo = [True for _ in range(MAX)] ; esPrimo[0] = False ; esPrimo[1] = False
    divs = [None for _ in range(MAX)] ; divs[0] = 0 ; divs[1] = 1 ; divs[2] = 2
    primos = [2]
    for i in range(4, MAX, 2): esPrimo[i] = False ; divs[i] = 2
    
    for i in range(3, MAX, 2):
        if esPrimo[i]:
            divs[i] = i
            primos.append(i)
            for j in range(i * i, MAX, i):
                esPrimo[j] = False
                divs[j] = i
