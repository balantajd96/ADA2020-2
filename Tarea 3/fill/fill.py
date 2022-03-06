## Juan Diego Balanta
## id: 0220859
## 29 de Septiembre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
## Inspiración y Guia
## Notas de clase 2018-1
## 
## https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
## https://devcode.la/tutoriales/diccionarios-en-python/
## https://bhrigu.me/blog/2016/04/04/3-jug-problem-python-code/

from sys import stdin
from heapq import heappush,heappop

global maxA,maxB,maxC

def pour(weigth,fromJug,toJug,maxToJug):
	#recibo el agua que se ha pasado, junto a la primera y segunda jarra
	free_space = maxToJug - toJug
	#cuanta agua tengo disponible para vertir en toJug
	to_pour = min(fromJug,free_space)
	fromJug -= to_pour
	toJug += to_pour
	#regreso el agua que tenia mas lo que acabo de agregar en la otra jarra, y los nuevos estados de las jarras
	return weigth+to_pour,fromJug,toJug

def generateNode(node,i):
	#todas las posibles combinaciones de agua que se puede pasar de un "jug" a otro
	# donde: saco agua -> agrego agua
	global maxA,maxB,maxC
	weigth,a,b,c = node
	if i==0: # a -> b
		weigth,a,b = pour(weigth,a,b,maxB)
	if i==1: # a -> c
		weigth,a,c = pour(weigth,a,c,maxC)
	if i==2: # b -> a
		weigth,b,a = pour(weigth,b,a,maxA)
	if i==3: # b -> c
		weigth,b,c = pour(weigth,b,c,maxC)
	if i==4: # c -> a
		weigth,c,a = pour(weigth,c,a,maxA)
	if i==5: # c -> b
		weigth,c,b = pour(weigth,c,b,maxB)
	return weigth,a,b,c

def solve(aguaPasada,visitado,heap,d,cInicial):
	
	while(len(heap) != 0):
		node = heappop(heap)
 	    #weight representa la distancia necesaria para llegar al nodo
	    #que representa cuanta agua se movio de jarra en jarra independiente que jarra sea
		weigth,a,b,c = node	
		#si conocemos a y b podemos deducir c 
		#en la inicializacion se guarda el origen y luego se guarda cuanta agua se tuvo que utilizar
		if (a,b) not in visitado:
			visitado.add((a,b))
			aguaPasada[(a,b)] = weigth
         
			for i in range(6):
				#creamos las posibles combinaciones de agua, y revisamos si ya lo visitamos para no repetir nodos
				new_node = generateNode(node,i)
				weigth,a,b,c = new_node
				if (a,b) not in visitado:
					heappush(heap,new_node)
    #Al terminar de generar todas las posibles combinaciones recorro 
    # el diccionario para buscar la menor cantidad de agua usada junto a dPrima
	dCercano = 0
	minimaAgua = 0
	for a,b in visitado:
		#o me acerco mas a d o uso menos agua para llegar
		# no me interesa encontrar la jarra mas llena,
		# sino la jarra que tenga el valor d buscado inicialmente
		# por eso me interesa cual es la que este mas cerca al origen
		# para lograr el objetivo d con la menor cantidad de agua entre jarra y jarra
		weigth = aguaPasada[(a,b)]
		c = cInicial - a - b
		if a<=d and (a>dCercano or (a==dCercano and weigth<minimaAgua)):
			dCercano = max(dCercano,a)
			minimaAgua = weigth
		if b<=d and (b>dCercano or (b==dCercano and weigth<minimaAgua)):
			dCercano = max(dCercano,b)
			minimaAgua = weigth
		if c<=d and (c>dCercano or (c==dCercano and weigth<minimaAgua)):
			dCercano = max(dCercano,c)
			minimaAgua = weigth
	return minimaAgua, dCercano
		

def main():
	global maxA,maxB,maxC
	numCases = int(stdin.readline().strip())
	for i in range(numCases):
		a,b,c,d = [int(x) for x in stdin.readline().strip().split()]
		#visited hace un conjunto de nodos que ya se han visitado, representa a v
		visitado = set()
		#aguaPasada es un dictionario que te traduce cuanta agua se pasó para llegar a cada nodo (El peso de cada nodo)
		aguaPasada = dict()
		#inicializacion del heap quien es el que guarda que ya hemos visitado
	    # se inicializa con [(agua que ya se ha pasado, cantidad en A, cantidad en B, y el C lleno)]
		heap = [(0,0,0,c)]
		#maxA,maxB,maxC representan la maxima cantidad de agua en cada "jug"
		maxA,maxB,maxC = a,b,c
		#minimaAguaPasada es el resultado de cuanta agua se paso al final para lograr dPrima quien es el valor más cercano a d
		if c<=d:
			print(0,c)
		elif a>=c and b>=c:
			print(0,0)
		else:
			minimaAguaPasada,dPrima = solve(aguaPasada,visitado,heap,d,c)
			print(minimaAguaPasada,dPrima)

main()
