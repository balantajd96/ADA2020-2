#Juan Diego Balanta
# Septiembre 12 de 2020
# punto 1.d bonus parcial 1
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from math import *
ejemplo=[9, 7, 7, 2, 5,1, 3,  4, 7, 3, 3, 4, 8, 6, 9] #entrada del ejercicio del libro
#ejemplo=[9, 10, 1] #ejempplos

#ejemplo=[7,5,7,7,2,3] #tanto 5 como 2 es un minimo local
#
#  Ciclo para recorrer y obtener en O(n) TODOS LOS MINIMOS LOCALES
#  for a in range(1, n-1):
#             if arreglo[a-1]>=arreglo[a] and arreglo[a]<=arreglo[a+1]:
#                 print (arreglo[a])
#------------------PARA ESTA SOLUCION-------------
# lo importante es que entregue al menos un minimo local, ya que el problema no especifica que se entreguen todos los minimos locales, 
# de ser así el caso, entonces se debería recorrer todo el arreglo, y eso es una solución O(n)
# esta solucion es O(log n) ya que cada vez se está verificando en un arreglo mucho más pequeño al anterior hasta llegar a la solución.

def localMinimum(arreglo):
    n=len(arreglo)
    #print("El tamaño de ", arreglo, " es: ", n)
    mitad = ceil(n//2)
    #print ("El arreglo particionado es: ", arreglo)
    if (n == 3 and arreglo[0]>=arreglo[1] and arreglo[1]<=arreglo[2]):
        return arreglo[1]
    if mitad+1 == n and arreglo[mitad-1] >= arreglo[mitad]:#esto funciona ya que al partisionar el arreglo, arreglo[mitad+1] es mayor o igual a arreglo[mitad]
        return arreglo[mitad]
    if (arreglo[mitad]<arreglo[mitad+1]):
        return localMinimum(arreglo[0:mitad+1])
    else:
        return localMinimum(arreglo[mitad:n-1])


def main(arreglo):#FILTRO DE ENTRADAS DE ARREGLOS VALIDOS
    total=len(arreglo)
    if (total>1 and arreglo[0]>=arreglo[1] and arreglo[total-2]<= arreglo[total-1]):#filtra arreglos vacios y arreglos de dos elementos que sean diferentes
        print("El elemento:",localMinimum(arreglo), "es un minimo local del arreglo ",arreglo)
    else:
        if total==0:print ("El arreglo esta vacio")
        print("¡El arreglo ",arreglo," no cumple las condiciones iniciales!")



main(ejemplo)
