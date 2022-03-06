from sys import stdin
from math import *
## Juan Diego Balanta Posso
## 19 de Agosto de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
## Inspiración y Guía
## Teorema Crossed Ladders Problem
## https://brilliant.org/wiki/crossed-ladders-problem/

EPS=1e-9
#CASO BASE
# 26.033
# 7.000
# 8.000
# 9.798
def teoremaCrossedLadder(xLadder,yLadder,street):
  ##   1/h = 1/h1 + 1/h2
  ## x**2 = h1**2 + calle**2 
  ## y**2 = h2**2 + calle**2  
  return 1/sqrt(xLadder**2-street**2) + 1/sqrt(yLadder**2-street**2)  


def solve(x, y, c):
  ans = 0
  # place your code here!
  #print(x,y,c)
  low=0
  hi=min(x,y)
  # teorema representa al valor dado en el teorema de crossedLadders = 1/h
  teorema = 1/c
  while(hi-low>EPS):
    calle=(hi+low)/2#representa el valor de la calle o la mitad de la busqueda entre hi y low
    #si 1/h1 + 1/h2 < 1/h no se ha encontrado el valor de la distancia de la calle
    if (teoremaCrossedLadder(x,y,calle))<teorema:
      low = calle
    else:
      hi=calle
  ans=calle
  return ans

def main():
  line = stdin.readline()
  while len(line)!=0:
    x,y,c = map(float, line.split())
    print('{0:.3f}'.format(solve(x, y, c)))
    line = stdin.readline()

main()
