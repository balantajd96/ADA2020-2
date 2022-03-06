from sys import stdin
from math import *

#if(i == numCases -1):
            #Si la cadena es impar
            #print("If:",i, numCases)
            #print("la cadena es:",line, "la i es:",i, "la numcases es:",numCases)
            #print(solve(line,n)-1)
        #else:
            #print("Else:",i, numCases)









def main():
    line =stdin.readline().split()
    while(line!=[]):    
        n,m = map(int, line)
        arreglo = [ int(x) for x in stdin.readline().split() ]
        suma=sum(arreglo)
        print(int(solveMax(n, m, arreglo, suma)))#, int(solveMin(n,m,arreglo)))
        line =stdin.readline().split() 