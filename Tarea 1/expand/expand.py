## Juan Diego Balanta Posso
## 19 de Agosto de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
## Inspiración y Guía
## Robin Quintero y Sesión de Dividir, Conquistar y Combinar (08/13) min 1:52:21

from sys import stdin
from math import *
EPS=1e-9
#RESPUESTA BASE
# 61.329
# 225.020
# 0.000

def solve(L, n, C):
  ans = 0
  # place your code here!
  # Representación de L'
  expansion = (1+n*C)*L
  #alpha viene siendo el angulo 
  #low se utiliza en la iteración para encontrar el valor de alpha
  alpha,low=0,0
  # al ser un cuarto de circunferencia
  # la función en radianes va desde 
  # [low,hi]=[0,pi/2]
  hi=pi/2

  while (hi-low > EPS): #hasta que llegue al punto más pequeño
    alpha = (low+hi)/2
    #print ("El alpha es:",alpha)
    R=L/2/(sin(alpha))
    a = (2*R*alpha ) 
    #print("El resultado de alpha es:", alpha)
    #print("El resultado de a es:", a)
    #print("El resultado de R es:", R)
    if(a < expansion):
      low = alpha
    else:
      hi = alpha
  #ans = la distancia h que se forma entre R = radio calculado del circulo
  #y para r quien logra un triangulo de pitagoras
  ans = R-R*cos(alpha) 
  return ans


def main():
  #clen = initial lenght of the rod
  #tmpc = cambio de temperatura
  #hec = coeficiente de expansion
  clen,tmpc,hec = [ float(x) for x in stdin.readline().split() ]
  while clen>=0 and tmpc>=0 and hec>=0:
    print('{0:.3f}'.format(solve(clen, tmpc, hec)))
    clen,tmpc,hec = [ float(x) for x in stdin.readline().split() ]

main()
