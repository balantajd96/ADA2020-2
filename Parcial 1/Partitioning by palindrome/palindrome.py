#Juan Diego Balanta
#14 de Septiembre 2020
# id: 0220859
#Guia de resolucion:
#https://www.youtube.com/watch?v=lDYIvtBVmgo

from sys import stdin
INF = float("inf")

def esPalindrome(line): #Funcion hecha para verificar que palabra es palindrome
    ans = True
    n = len(line)
    for i in range(0,n):
        #Se utiliza el for para verificar los extremos de la palabra y asi identificar si es palindrome
        # en el caso en el que la palabra no sea palindrome, en algun extremo, deja de verificar y se debe cortar la palabra  
        if line[i] != line[n-1-i] and (ans==True):
            ans = False
            i=n
    return ans
     
def solve(line,n):
    tab = [INF] * (n+1) ## lleno tab para comenzar
    #print("la cadena es:",line)
    tab[0] = 0 #Inicializacion
    #print("la memoria es:",tab)
    for i in range(1,n+1): ## rango del arreglo
        for j in range(0,i):
            if (esPalindrome(line[j:i])): ## particion de la lista line para preguntar si esa parte es palindrome o no
                #el rango va desde j hasta i ya que i viene siendo la parte de la cadena que se esta comparando
                tab[i] = min(tab[i],1+tab[j]) ## verifico cual es la minima particion entre la particion anterior, como decir, corto o no corto la cadena
    #print("El final es:",tab)
    return tab[n-1] #se debe de recoger el ultimo elemento ya que así se ha verificado toda la cadena la cual devuelve cuantas veces se ha cortado
     
def main():
    global dataIn,line
    dataIn = stdin
    numCases = int(dataIn.readline())
    #print(numCases)
    for i in range(0,numCases):
        line = dataIn.readline()
        n = len(line)
        # if(i == numCases -1):
        #     Si la cadena es impar
        #     #print("If:",i, numCases)
        #     #print("la cadena es:",line, "la i es:",i, "la numcases es:",numCases)
        #     print(solve(line,n)-1)
        # else:
        #     print("Else:",i, numCases)
        print(solve(line,n))
main()

 