## Juan Diego Balanta Posso
## 15 de Septiembre de 2020
## id: 0220859
## 
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin
from math import *


def solve(cadena):
    k,S=cadena[0][0],list(cadena[0][1])
    #print("El entero k es:", k, "la cadena es:", S)
    S.sort()
    print(S)
    ##primer caso cuando m = M se devuelve 0

    ##segundo caso cuando m!=M and c no pertenece T[m]

    ##tercer caso cuando m!=M and c es igual al elemento en T[m]

    ##cuarto caso cuando m!=M and c no está contenido en T[m]








def main():
    numCasos = int(stdin.readline())
   
    for i in range(numCasos):
        caso=[]
        entrada = stdin.readline().split()
        #print(caso)
        #print("Entrada",entrada)
        caso.append([int(entrada[0]),str(entrada[1])])
        #print("CASO CON VALORES:",caso)
        print(solve(caso))

main()