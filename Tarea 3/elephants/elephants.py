## Juan Diego Balanta Posso
## 19 de Septiembre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin



def solve(M,W,arreglo):
    subidos,pesoAcumulado=0,0
    arreglo.sort()
    #print("El numero y peso son",M,W)
    for i in range(M):
        #print("El elefante",arreglo[i])
        #print("Resistencia telarania:", W-pesoAcumulado)
        if arreglo[i] <= (W-pesoAcumulado):
            subidos+=1
            pesoAcumulado+=arreglo[i]
        else:
            return subidos
             
    return subidos

def main():
    numcases = int(stdin.readline())
    #print("El numero de casos es: ",numcases)
    for i in range(numcases):
        m,w=map(int, stdin.readline().split())
        elefantes=[int(x) for x in stdin.readline().split()]
        #print(elefantes)
        #print("El caso",i, "es: ", "\nCantidad de elefantes:",m, "\nPeso de la telarania es: ",w,"\nEstos elefentates se balanceaban:",elefantes)
        print(solve(m,w,elefantes))
main()