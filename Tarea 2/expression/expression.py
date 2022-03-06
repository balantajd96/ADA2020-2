from sys import stdin
## Juan Diego Balanta Posso
## 9 de Septiembre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.


NINF,INF = float('-inf'),float('inf')



def solveMax(n,m,arreglo):
    ansMax=None
    sumaTotal=sum(arreglo)
    #print("El n es:", n, "el m es:", m, "el arreglo contiene", arreglo, "la suma del arreglo es: ",sumaTotal)
    
    arreglo.sort()
    tabulacion=[[INF for _ in range(m+1)] for _ in range(n+m)]
    
    for i in range(n+m):
        tabulacion[i][0]=sumaTotal
    tabulacion[0][1]=abs(sumaTotal-2*arreglo[0])
    #print(tabulacion)
    for i in range(1,n+m):
        for j in range(1,m+1):
            noAgregoX=tabulacion[i-1][j]#celda de la izquierda sin elegir un numero para Y
            agregoX=abs(tabulacion[i-1][j-1]-2*arreglo[i])
            tabulacion[i][j]= min(noAgregoX,agregoX)
    minimaDiferencia = tabulacion[n+m-1][m]
    conjuntoX=(sumaTotal-minimaDiferencia)/2
    conjuntoY=(sumaTotal-conjuntoX)
    return conjuntoX*conjuntoY

def solveMin(n,m,arreglo):
    ansMax=None
    sumaTotal=sum(arreglo)
    #print("El n es:", n, "el m es:", m, "el arreglo contiene", arreglo, "la suma del arreglo es: ",sumaTotal)
    
    arreglo.sort()
    tabulacion=[[NINF for _ in range(m+1)] for _ in range(n+m)]
    
    for i in range(n+m):
        tabulacion[i][0]=sumaTotal
    tabulacion[0][1]=abs(sumaTotal-2*arreglo[0])
    #print(tabulacion)
    for i in range(1,n+m):
        for j in range(1,m+1):
            noAgregoX=tabulacion[i-1][j]#celda de la izquierda sin elegir un numero para Y
            agregoX=abs(tabulacion[i-1][j-1]-2*arreglo[i])
            tabulacion[i][j]= max(noAgregoX,agregoX)
    minimaDiferencia = tabulacion[n+m-1][m]
    conjuntoX=(sumaTotal-minimaDiferencia)/2
    conjuntoY=(sumaTotal-conjuntoX)
    return conjuntoX*conjuntoY


def main():
    line =stdin.readline().split()
    while(line!=[]):    
        n,m = map(int, line)
        arreglo = [ int(x) for x in stdin.readline().split() ]
        print(int(solveMax(n, m, arreglo)),int(solveMin(n, m, arreglo)))
        line =stdin.readline().split()      

main()