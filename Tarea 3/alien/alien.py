## Juan Diego Balanta Posso
## 25 de Septiembre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin



# def solve(numero,arreglo):
#     print("Entraron ",numero, "cadenas de DNA:",arreglo)
def solve(numero,arreglo):
    #es igual a la cantidad de cortes 
    minCuts=0
    comparte=arreglo[0]
    for elemento in arreglo:
        if(len(comparte.intersection(elemento))==0):
            minCuts+=1
            comparte=elemento
        else:
            comparte=comparte.intersection(elemento)
    return minCuts



    



def main():
    numCases = int(stdin.readline())
    #print("El numero de casos es: ",numcases)
    for i in range(numCases):
        numCadenas=int(stdin.readline().strip())
        cadenasDNA=[set(stdin.readline().strip()) for x in range(numCadenas)]
        #print(elefantes)
        #print("El caso",i+1, "es:\n")
        print(solve(numCadenas,cadenasDNA))

main()