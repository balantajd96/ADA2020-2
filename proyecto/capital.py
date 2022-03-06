## Juan Diego Balanta Posso
## PROYECTO DESIGN NEW CAPITAL
## 7 de Noviembre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin
from math import *

MODULE = 7340033
root=5
root_1 = 4404020
rootPower = 1<<20
N = 100001

# Arreglo utilizado para los inversos del factorial hasta N
factorialNumInverse = [None] * (N + 1)
# Arreglo que guarda los inversos del entero hasta N
naturalNumInverse = [None] * (N + 1)
# Arreglo que guarda los factoriales hasta N
preFactorial = [None] * (N + 1)
 
def precalculations(module):
    """
        Entrada: valor entero positivo
        Salida: precalcula los factoriales, su inverso para poder utilizarlos en el calculo de los coeficientes binomiales
    """
    preFactorial[0] = factorialNumInverse[0] = factorialNumInverse[1] = naturalNumInverse[0] = naturalNumInverse[1] = 1
    
    # precomputo de los factoriales inversos con el natural inverso y factoriales normales
    for i in range(2, N + 1):
        naturalNumInverse[i] = (naturalNumInverse[module % i] * (module - module // i) % module)
        factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % module    
        preFactorial[i-1] = (preFactorial[i - 2] * (i-1)) % module

    

def binomialCoefficients(n, k):
    """
         entrada: n y k quienes representan a los valores C(n,k) 
         o la forma de tomar k valores en un conjunto n

         salida: el resultado de la operacion C(N,K)

         la funcion utiliza la propiedad de factorial para resolver el coeficiente
         lo que hace es tomar los valores precalculados para resolverlo de manera constante
         por medio de la formula C(n,k) = n!inverse(k!)inverse((n-k)!)
         
    """
    ans = ((preFactorial[n] * factorialNumInverse[k])% MODULE * factorialNumInverse[n-k])% MODULE
    return ans

#precalculos que ayudan a que se hagan las consultas en O(1), tema investigado en GeekForGeeks
precalculations(MODULE)



####################################################################################################################################
def modInv( x, M):
    #Basado en el EXTENDED EUCLIDEAN ALGORITHM para MODULAR INTEGER WIKIPEDIA
    t, new_t, r, new_r = 0, 1, M, x

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, (t - quotient * new_t)
        r, new_r = new_r, (r % new_r)
    if t < 0:
        t = t + M
    return t

def NTT(polinomio,inversa):
    """
        Entrada: a esta funcion le entra un arreglo de valores enteros los cuales representan al polinomio resultante de las combinatorias entre los cuadrantes opuestos
                 y un valor booleano el cual dicta si se debe realizar la inversa (Si el valor es False) de la transformación o la normal (Si el valor es True).

        Salida: El resultante es un polinomio que contiene los valores de la transformacion NTT 

        
        Esta funcion se basa en la Number Theoretic Transformation la cual es una transformada de Fourier utilizada para valores enteros con la propiedad de Wn= 1 mod p 
        sin transformar las entradas a numeros complejos para así evitar las imprecisiones de trabajar con numeros flotantes.  

    """
    n=len(polinomio)
    
    j=0
    for i in range(1,n):
        bit = n>>1
        while j&bit:
            j=j^bit
            bit=bit>>1
        j=j^bit
        
        if i < j:
            temp = polinomio[i]
            polinomio[i]=polinomio[j]
            polinomio[j]=temp
    lent=2
    
    while(lent<=n):
        if inversa:
            wlen=root_1
        else:
            wlen=root
        j=lent
        while(j<rootPower):
            wlen=int((wlen*wlen)%MODULE)
            j<<=1
        i=0
        
        while(i<n):
            w=1
            j=0
            while(j < (lent>>1)):
                u=polinomio[j+i]
                v=int(polinomio[j+i+lent//2]*w%MODULE)
                if (u+v<MODULE):
                    polinomio[j+i]=u+v
                else:
                    polinomio[j+i]=u+v-MODULE
                if(u-v>=0):
                    polinomio[j+i+lent//2]=u-v
                else:
                    polinomio[j+i+lent//2]=u - v + MODULE
                w=int((w*wlen)%MODULE)
                j+=1
            i+=lent
        lent=lent<<1
        
    if inversa:
        invert=modInv(n,MODULE)
        for i in range(len(polinomio)):
            polinomio[i]=(polinomio[i]*invert%MODULE)
        
    return polinomio
     
def multiplicationPolinomials(polA_C,polB_D):
    """
        Entrada: Dos arreglos de numeros enteros, 
                        polA_C quien es un arreglo de numeros enteros que representa a los coeficientes de un polinomio
                        polB_D quien es un arreglo de numeros enteros que representa a los coeficientes de un polinomio
        
        Salida: como resultante es un arreglo de valores enteros el cual representa un polinomio

        Esta funcion toma los valores de los polinomios y los multiplica entre ellos
    """
    #n representa el tamanio del polinomio de potencia 2, nElementsAC,nElementsBD
    n,nElementsAC,nElementsBD = 1, len(polA_C),len(polB_D)
    while(n<nElementsAC+nElementsBD):
        n=n<<1
    #Redimension del polinomio respectivo de los cuadrantes A y C o 1 y 3
    for i in range(n-nElementsAC):
        polA_C.append(0)
    #Redimension del polinomio respectivo de los cuadrantes B y D o 2 y 4
    for i in range(n-nElementsBD):
        polB_D.append(0)
    #CALCULO DE LA TRANSFORMADA PARA ENTEROS, NUMERIC TRANSFORMATION 
    polynomial1=NTT(polA_C,False)
    
    polynomial2=NTT(polB_D,False)
    for i in range(n):
        polynomial1[i]=polynomial1[i]*polynomial2[i]
    #CALCULO DE LA TRANSFORMADA INVERSA PARA OBTENER EL POLINOMIO RESULTANTE DE LA MULTIPLICACION
    polynomial1=NTT(polynomial1,True)
    return polynomial1

def solve(firstQuadrant,secondQuadrant,thirQuadrant,fourthQuadrant):
    """
        Entrada:
        las variables utilizadas son las siguientes:
            firstQuadrant   = representa la cantidad de puntos que hay en el cuadrante 1 de un plano cartesiano
            secondQuadrant  = representa la cantidad de puntos que hay en el cuadrante 2 de un plano cartesiano
            thirQuadrant    = representa la cantidad de puntos que hay en el cuadrante 3 de un plano cartesiano
            fourthQuadrant  = representa la cantidad de puntos que hay en el cuadrante 4 de un plano cartesiano
        Salida: la salida es la cantidad de posibilidades para aceptar desde 1 hasta firstQuadrant+secondQuadrant+thirQuadrant+fourthQuadrant propuestas

        la funcion crea los polinomios del cuadrante 1 y 3 junto a 2 y 4, utiliza la trasnformada NTT para la multiplicacion de los polinomios

    """
    #creacion del polinomio entre el cuadrante 1 y cuadrante 3
    cuadranteA_C=min(firstQuadrant,thirQuadrant)
    polA_C=[]
    for i in range(cuadranteA_C+1):
        valor=(binomialCoefficients(firstQuadrant,i))*(binomialCoefficients(thirQuadrant,i))
        valor = valor%MODULE
        polA_C.append(int(valor))
    
    #creacion del polinomio entre el cuadrante 2 y cuadrante 4
    cuadranteB_D=min(fourthQuadrant,secondQuadrant)
    polB_D=[]
    for i in range(cuadranteB_D+1):
        valor=(binomialCoefficients(fourthQuadrant,i))*(binomialCoefficients(secondQuadrant,i))
        valor = valor%MODULE
        polB_D.append(int(valor))

    resultingPolynomial=multiplicationPolinomials(polA_C,polB_D)
    

    #IMPRIMIR RESULTADO
    ans=[]
    oddNumber=True    
    for i in range(1,firstQuadrant+secondQuadrant+thirQuadrant+fourthQuadrant+1):
        if oddNumber:
            ans.append(0)
        else:
            if i//2<len(resultingPolynomial):
                ans.append(resultingPolynomial[i//2])
            else:
                ans.append(0)
        oddNumber=(not oddNumber)        
    
    print(" ".join([str(x)for x in ans]))
   
def main():
    """
        Entrada: Funcion principal de inicializacion donde se obtendran todos los elementos del archivo capital.in
        por medio de stdin para pasar a la funcion de solucion llamada solve.

        Salida: el output del problema donde imprime el numero del Caso x: seguido de los valores que puede tomar desde 1 propuesta hasta numProposes

        numCases     = representa el valor T del problema donde T<=5
        numProposes  = representa el valor n de propuestas donde (1<= n <= 10^5)
        tok          = obtendra temporalmente la lectura de cada coordenadas x,y donde (-10^9<=x, y<=10^9) and (x*y != 0)
        los puntos se organizan en sus respectivos cuadrantes para dividirlo como:
            firstQuadrant   = representa la cantidad de puntos que hay en el cuadrante 1 de un plano cartesiano
            secondQuadrant  = representa la cantidad de puntos que hay en el cuadrante 2 de un plano cartesiano
            thirQuadrant    = representa la cantidad de puntos que hay en el cuadrante 3 de un plano cartesiano
            fourthQuadrant  = representa la cantidad de puntos que hay en el cuadrante 4 de un plano cartesiano
              
    """
    numCases = int(stdin.readline())
    #print("he recibido",numCases, "en total")
    for i in range(numCases):
        proposes = []
        firstQuadrant,secondQuadrant,thirQuadrant,fourthQuadrant = 0,0,0,0
        numProposes = int(stdin.readline())
        for j in range(numProposes):
            tok = [int(x) for x in stdin.readline().split()]
            if tok[0]*tok[1] > 0:
                if tok[0] > 0 and tok[1] > 0:
                    # si ambas coordenadas son positivas se encuentra en el primer cuadrante
                    firstQuadrant+=1
                else:
                    # de lo contrario significa que ambas son negativas ya que 
                    # -x*-y > 0
                    thirQuadrant+=1
            else:
                #si el valor es negativo entonces significa
                if tok[0] < 0: 
                    #que o el x es negativo lo que lo posiciona en el segundo cuadrante 
                    secondQuadrant+=1
                else:
                    #o el y es negativo lo que lo posiciona en el cuarto cuadrante
                    fourthQuadrant+=1
            #proposes.append((tok[0], tok[1]))
        print("Case {case}:".format(case=i+1))
        firstQuadrant=firstQuadrant%MODULE
        secondQuadrant=secondQuadrant%MODULE
        thirQuadrant=thirQuadrant%MODULE
        fourthQuadrant=fourthQuadrant%MODULE
        solve(firstQuadrant,secondQuadrant,thirQuadrant,fourthQuadrant)

main()
