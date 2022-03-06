## Juan Diego Balanta Posso
## 19 de Agosto de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
## Inspiración y Guía
## Introduction_to_algorithms-3rd Edition Authors. Cormen, Leiserson, Rivest, Stein

from sys import stdin
from math import *

MAX,EPS,INF = 100001,1e-9,float('inf')
ptsh = []



#SALIDA DE CASOS BASE
#INFINITY
#36.2215

def funcionDistancia(x1,y1,x2,y2):
  #FUNCION QUE CALCULA UNA DISTANCIA
    distancia=sqrt((x2-x1)**2 + ((y2-y1)**2))
    return distancia 

def solve(low, hi):
  global ptsh
  ans = INF
  
  if (hi-low)<=3:
    
    for i in range(low, hi):
      for j in range(i+1,hi):
        #print ("El iterador i es:",i)
        #print ("El iterador j es:",j)
        #print (ptsh[i][0],ptsh[i][1],ptsh[j][0],ptsh[j][1])
        ans=min(funcionDistancia(ptsh[i][0],ptsh[i][1],ptsh[j][0],ptsh[j][1]),ans)
        #print ("La distancia es:", minimo)
        #print ("el minimo actual es:", ans)
        #ans = min(minimo,ans)
  else:#divide and conquer
    mitad=low + ((hi-low)>>1)
    #print (" la mitad es:",mitad)
    minimoIzquierda = solve(low,mitad)
    minimoDerecha = solve(mitad,hi)

    distanciaActual = min(minimoIzquierda,minimoDerecha)
    ans = distanciaActual
    ptsaux=[]
    # for i in range(low,hi):
    #   if(abs(ptsh[mitad][0]-ptsh[i][0])<=distanciaActual):
    #     ptsaux.append(ptsh[i])
    i = mitad-1
    while i >= low:
      if(ptsh[mitad][0]-ptsh[i][0] <= distanciaActual ):
        ptsaux.append(ptsh[i])
      else:
        break
      i-=1
    i = mitad
    while i < hi:
      if ptsh[i][0]-ptsh[mitad][0] <= distanciaActual:
        ptsaux.append(ptsh[i])
      else:
        break
      i+=1
    ptsaux.sort(key=lambda x: x[1])

    medios=len(ptsaux)
    for j in range(medios-1):
      ans = min(funcionDistancia(ptsaux[j][0],ptsaux[j][1], ptsaux[j+1][0],ptsaux[j+1][1]),ans)
  return ans         

def main():
  global ptsh
  lenp = int(stdin.readline())
  while lenp!=0:
    ptsh= []
    #print ("ptsh es: " + str(ptsh) + "ptsv es:" + str(ptsv))
    while len(ptsh)!=lenp:
      tok = stdin.readline().split()
      ptsh.append([float(tok[0]),float(tok[1])])
     # ptsv.append(ptsh[-1])
    ptsh.sort(key=lambda x: x[0])
    #print(ptsh)
    #print ("ptsh es: " + str(ptsh) + "ptsv es:" + str(ptsv))
    #for i in range(len(ptsh)): ptsh[i][2] = i
    #print(ptsh)
    #ptsv.sort(key=lambda x: x[0])
    ans = solve(0,len(ptsh))
    if ans < 10000:
      print('{:.4f}'.format(ans))
    else:
      print('INFINITY')
    lenp = int(stdin.readline())

main()
