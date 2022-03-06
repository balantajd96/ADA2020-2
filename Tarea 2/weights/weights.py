## Juan Diego Balanta Posso
## 2 de Septiembre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin
from math import *
INF = float('inf')
    #weight = initial weight of the turtle
    #strength = how much do you lift bro

    #turtle[0]= weight
    #turtle[1]= strength
def solve(turtles):
    #turtle representa el elemento de cada posición, es decir cada tortuga
    prueba =[]
    prueba = sorted(turtles,key=lambda x: (x[1],x[0]))
    N = len(prueba)
    #tabTortuga es el metodo de Tabulacion, tabla con las respuesta de las comparaciones
    #i equivale al contador el cual me mueve en las filas 
    #  es la tortuga base de la "torre"
    #k equivale al contador el cual me mueve en las columnas, 
    #   es decir, k representa el numero de tortugas apiladas
    #ans equivale a la solucion del algoritmo
    ans=0
    #inicializo la tabla
    tabTortuga = [ [ INF for _ in range(N+1) ] for _ in range(N) ]
    #casilla inicial de la primera tortuga
    if prueba[0][1] >= prueba[0][0]:
        tabTortuga[0][1]=prueba[0][0]
    for i in range(N):
        tabTortuga[i][0]=0
    #print(prueba[0][0])
    #print()
    #print (tabTortuga) NO SE ENOJE PROFE, LO QUIERO
    i,k=1,1
    while (i < N):#este ciclo va a recorrer cada tortuga como base
        #jugando jenga con las tortugas
        while(k < N+1):    
            #condición para ver si puede cargar la tortuga y a ella misma
            if prueba[i][0] + tabTortuga[i-1][k-1] < prueba[i][1]:
            #se sacan los pesos de las tortugas pasadas
            #  prueba[k-1][0]+tabTortuga[i-1][0] utiliza el peso de la tortuga si se apila más la siguiente
                noAgregoTortuga= tabTortuga[i-1][k]
                siAgregoTortuga= tabTortuga[i-1][k-1]+prueba[i][0]
                #encuentro quien es el minimo para tener mas tortugas apiladas
                tabTortuga[i][k] = min(noAgregoTortuga, siAgregoTortuga) 
            else:
                tabTortuga[i][k] = tabTortuga[i-1][k]
            #condición para cambiar el maximo de tortugas hasta ahora
            if tabTortuga[i][k] != INF and ans < k: ans=k
            k+=1
#        print ("van apiladas ",ans,"tortugas") NO SE ENOJE PROFE, LO QUIERO
    #    print (ans)
        k=1
        i+=1
#    print ("La tablita de la suerte:") NO SE ENOJE PROFE, LO QUIERO
#    print (tabTortuga) NO SE ENOJE PROFE, LO QUIERO
    #print ("sin organizar: ",turtles) NO SE ENOJE PROFE, LO QUIERO
    # print ("organizadas: ", prueba) NO SE ENOJE PROFE, LO QUIERO
    # for turtle in turtles:
    #     print("El peso es:",turtle[0], ", La fuerza es:", turtle[1], " puede cargar:", turtle[1]-turtle[0])
    return ans

  
    


def main():
  #weight = initial weight of the turtle
  #strength = how much do you lift bro
  entrada =stdin.readline()
  tortugas=[]
  while len(entrada)!=0:
    weight,strength = [ int(x) for x in entrada.split() ]
    tortugas.append([weight,strength])
    entrada = stdin.readline()
  print(solve(tortugas))
main()