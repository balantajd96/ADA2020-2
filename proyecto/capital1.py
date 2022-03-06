## Juan Diego Balanta Posso
## PROYECTO DESIGN NEW CAPITAL
## 7 de Noviembre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin
#from math import comb
INF = float('inf')

def binomialCoefficients(n,k):
    """
        entrada: n y k quienes representan a los valores C(n,k) 
        o la forma de tomar k valores en un conjunto n

        la funcion utiliza la propiedad de factorial para resolver el coeficiente
        lo que hace es realizar las divisiones individuales de cada valor
        coef_bin = representa el valor acumulado del coeficiente binomial
    """
    if(k > n - k): 
        k = n - k 
    #se inicializa ya que el valor base es 1
    coef_bin = 1
    #se sigue la idea de recursion de 
    for i in range(k): 
        coef_bin = coef_bin * (n - i) 
        coef_bin = coef_bin / (i + 1) 
    return coef_bin   
  




def solve(firstQuadrant,secondQuadrant,thirQuadrant,fourthQuadrant):
    """
        
        Entrada:
        las variables utilizadas son las siguientes:
            firstQuadrant   = representa la cantidad de puntos que hay en el cuadrante 1 de un plano cartesiano
            secondQuadrant  = representa la cantidad de puntos que hay en el cuadrante 2 de un plano cartesiano
            thirQuadrant    = representa la cantidad de puntos que hay en el cuadrante 3 de un plano cartesiano
            fourthQuadrant  = representa la cantidad de puntos que hay en el cuadrante 4 de un plano cartesiano
        Salida: la salida es la cantidad de posibilidades para aceptar desde 1 hasta firstQuadrant+secondQuadrant+thirQuadrant+fourthQuadrant propuestas

        variables función:
            cuadranteA_C toma el minimo entra los cuadrantes 1 y 3 para hacer la combinatoria desde k = 0 hasta el minimo numero de puntos en ambos cuadrantes para cumplir la condicion de tomar igual cantidad de opuestos
            cuadranteB_D es igual para cuadrante 2 y 4
            polA_C contiene los valores del "polinomio" del cuadrante 1 y 3
            polB_D contiene los valores del "polinomio" del cuadrante 2 y 4
            res contiene la multiplicacion de polA_C y polB_D        

    """
    cuadranteA_C=min(firstQuadrant,thirQuadrant)
    polA_C=[]
    for i in range(cuadranteA_C+1):
        valor=(binomialCoefficients(firstQuadrant,i))*(binomialCoefficients(thirQuadrant,i))
        #valor=(comb(firstQuadrant,i))*(comb(thirQuadrant,i))
        polA_C.append(int(valor))
    #print(polA_C)
    
    cuadranteB_D=min(fourthQuadrant,secondQuadrant)
    polB_D=[]
    for i in range(cuadranteB_D+1):
        valor=(binomialCoefficients(fourthQuadrant,i))*(binomialCoefficients(secondQuadrant,i))
        #valor = (comb(fourthQuadrant,i))*(comb(secondQuadrant,i))
        polB_D.append(int(valor))
    #print(polB_D)
    
    res=[0 for x in range(len(polA_C)+len(polB_D)-1)]
    #print(res)
    ##Multiplicacion de poliniomios fuerza bruta se guarda en res
    for i in range(len(polA_C)):
        for j in range(len(polB_D)):
            res[i+j]+=polA_C[i]*polB_D[j]
    
    #print("polinomio resultante")
    #ans contiene el polinomio resultante de la multiplicacion
    ans=[]
    oddNumber=True
    #en este caso proposes no es tan necesario ya que es igual de equivalente decir range(1,(firstQuadrant+secondQuadrant+thirQuadrant+fourthQuadrant+1))
    for i in range(1,firstQuadrant+secondQuadrant+thirQuadrant+fourthQuadrant+1):
        if oddNumber:
            ans.append(0)
        else:
            if i//2<len(res):
                ans.append(res[i//2])
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
        solve(firstQuadrant,secondQuadrant,thirQuadrant,fourthQuadrant)


main()
