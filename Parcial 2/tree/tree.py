## Juan Diego Balanta Posso
## 26 de Octubre de 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
#cantidad maxima del ejercicio

MAXN=10000


from sys import stdin
import time
def solve(marble,children,stack,tree):
    #Cada vez que saco canicas de los hijos debo "botarlas" 
    # todas en el padre cercano pero dejar al menos 1 canica 
    # siempre ya que no debo de tener hijos vacios, pero en el caso de que los tenga
    # debo volver a iterar sobre ese hijo hasta llenarlo
    marblesMoved = 0

    while len(stack)!= 0:
        #reviso el vertice pero debo quitarlo para que no tenga un bucle
        actualVertix =stack.pop()
        children[tree[actualVertix]] -= 1
        #como tengo varias canicas debo dejar al menos una sola
        marble[tree[actualVertix]] += marble[actualVertix] - 1
        if marble[actualVertix] > 0:
            marblesMoved += marble[actualVertix] -1    
        else:
            marblesMoved += 1- marble[actualVertix]
        #si no lo pude llenar tengo que agregarlo de nuevo para llenarlo
        if children[tree[actualVertix]] == 0 :
            stack.append(tree[actualVertix])
    return marblesMoved


def main():

    marble,children,tree = [None for i in range (MAXN)],[None for i in range (MAXN)],[None for i in range (MAXN)]
    nCases = int(stdin.readline().strip())
    while (nCases != 0):
        #inicializacion del arbol 
        tree = [0 for i in range(0,nCases)]
        emptyChildren = []
        for i in range (0,nCases):
            line = stdin.readline().split()
            #iVertex representa al vertice actual del input en el arreglo se ve como i-1
            iVertex = int(line[0])-1
            #cuantas canicas hay en ese vertice e hijos y children[iVertex] representa a d hijos en el vertice v o iVertex
            marble[iVertex],children[iVertex] = int(line[1]),int(line[2])
            #armo los hijos segun el vertice si son 0 debo llenarlos luego
            for child in line[3:]:
                #print("El hijo es:",child)
                tree[int(child)-1] = iVertex
            if (children[iVertex]== 0):
                #recorro de abajo hacia arriba el arbol 
                # para llenar las hojas vacias
                emptyChildren.append(iVertex)
        print(solve(marble,children,emptyChildren,tree))
        nCases = int(stdin.readline().strip())
#start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))