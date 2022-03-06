## Juan Diego Balanta
## id: 0220859
## 12 de Octubre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
from sys import stdin

def solve(n,m):
    minM=10**(m-1)
    while(len(str(minM))==m):
        i=n
        noEncontro=False
        #print(minM)
        while(i<=m):
            x=str(minM)
            x=int(x[0:i])
            if(x%i==0):
                i+=1
            else:
                noEncontro=True
                break
        if noEncontro:
            minM+=1
            # minM=str(minM)
            # digitoACambiar=minM[i-1]
            # digitoACambiar=int(digitoACambiar)+1
            # if digitoACambiar==10:
            #     break
            # else:
            #     minM=minM[0:i-1]+str(digitoACambiar)+minM[i:]
            #     minM=int(minM)
        else:
            break
    if noEncontro:
        return -1
    else:
        return minM
                    
def main():
    #cases=int(stdin.readline())
    #for i in range(cases):    
    line=[int(x) for x in stdin.readline().strip().split()] 
    #print(solve(line[0],line[1]))
    print("Case 1:",solve(line[0],line[1]))


main()