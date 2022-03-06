## Juan Diego Balanta Posso
## 25 de Septiembre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin

def solve(salaCine):
    #print("La sala de cine es:",salaCine)
    #print(len(salaCine))
    for i in range(len(salaCine)):
        conflicto=False
        for j in range(len(salaCine[0])):
            #El unico conflicto se presenta cuando la bebida se coloca a la derecha
            if salaCine[i][j]=='+':
                conflicto=True
            if conflicto==True:
                #Si la silla esta vacia '#' no hay conflicto ya que se puede colocar la bebida en ese espacio vacio
                if salaCine[i][j]=='#':
                    conflicto=False
                #en caso de que la silla tenga un vaso a la izquierda, se daña el ritual
                if salaCine[i][j]=='-':
                    return False
    #si recorro todo es porque no encontre ningun problema para el ritual        
    return True

def main():
    R,C = [int(x) for x in stdin.readline().strip().split()]
    contador=0
    while R!=0 and C!=0:
        cine = [["#" for columna in range(C)] for fila in range(R)]
        P = int(stdin.readline().strip())
        #Se inicializan los extraños en el cine
        for persona in range(P):
            filaColumna,bebida = stdin.readline().strip().split()
            fila = ord(filaColumna[0]) - ord("A")
            columna = int(filaColumna[1:])-1
            cine[fila][columna] = bebida
        #Se inicializan los amigos en el cine
        Z = int(stdin.readline().strip())
        for amigo in range(Z):
            filaColumna = stdin.readline().strip()
            fila = ord(filaColumna[0]) - ord("A")
            columna = int(filaColumna[1:])-1
            cine[fila][columna] = "P"

        if solve(cine):
            print("YES")
        else:
            print("NO")
        # if contador==17: NO ME ODIE PROFE
        #     print(cine)
        # contador+=1
        R,C = [int(x) for x in stdin.readline().strip().split()]

main()
