## Juan Diego Balanta Posso
## 15 de Septiembre 2020
## id: 0220859
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
## 

from sys import stdin
# from math import *
# from time import time #importamos la función t
EPS=1e-9

#def solve(tsum, diff): #Prueba de entrada de datos
   # print("Total Amount to Pay", tsum, "Absolute Value Difference", diff)

def americusToCwh(Value):
	##funcion para dividir la cuenta de cobro en energia
	precios=[[2,100], [3,9900], [5,990000]]
	conversion,i= 0,0
	while (i<3):#la cuenta de cobro es "acumulativa"   #TIMELIMIT
		#print("CONSUMO: i es:", i, "c es:", conversion,"Valor es:", Value)
		conversion += min(max(0,Value//precios[i][0]),precios[i][1])
		Value-=(precios[i][0]*precios[i][1])
		i+=1
	
	conversion+=max(0,Value//7)#si la división da menos de 0 no se le suma nada
	#print("el c final es:", conversion)
	return conversion

def cwhToAmericus(Value):
	##funcion para multiplicar el valor de la energia
	#print("cwhToAmericus", Value)
	precios=[[2,100], [3,9900], [5,990000]]
	conversion = 0
	if Value <= 100:
		conversion += Value*2
		Value = 0
	else:
			conversion += 200
			Value -= 100
			if Value <= 9900:
				conversion += Value*3
				Value = 0
			else:
				conversion += 9900*3
				Value -= 9900
				if Value <= 990000:
					conversion += Value*5
					Value = 0
				else:
					conversion += 990000*5
					Value -= 990000
					conversion += Value*7
	return conversion

	# while i<3:#la cuenta de cobro es "acumulativa"
	# 	#print("VALOR: i es:", i, "c es:", conversion,"Valor es:", Value)
	# 	conversion += precios[i][0]*min(max(0,Value),precios[i][1])
	# 	Value-=precios[i][1]
	# 	i+=1
	# conversion+=max(0,Value*7)#en caso de negativo no se suma
	# #print("el c final es:", conversion)
	# return conversion

def solve(tsum, diff):
	totalEnergiaJunta = americusToCwh(tsum)
	low = 0 #mi gasto
	hi = totalEnergiaJunta #el gasto del vecino
	#print("La primera mitad",low+(hi-low)>>1)
	while low+1<hi:
		mid = low+((hi-low)>>1)
		#print(mid)
		#### 300 = |350 - 650|
		consumo = cwhToAmericus(mid)
		diferencia = cwhToAmericus(totalEnergiaJunta - mid) - consumo
		#print("cwhToAmericus(totalEnergiaJunta - mid)",cwhToAmericus(totalEnergiaJunta - mid))
		#print("cwhToAmericus(mid)", cwhToAmericus(mid))
		#print(diferencia)
		if diferencia <= diff: hi = mid
		else:
			low=mid		
	return cwhToAmericus(hi)	
	
			

	

def main():
	# tsum es el absoluto de ambos gastos de energia
	# diff es el valor de la diferencia entre la factura tuya y del vecino
	tsum,diff = map(int,stdin.readline().split())
	while tsum+diff!=0:
		#print("el valor de tsum es:",tsum)
		#print("el valor de diff es:",diff)
		print(solve(tsum, diff))
		tsum,diff = map(int,stdin.readline().split())
#print("Si consumes 10123 CWh debes pagar :", cwhToAmericus(10123)) 				 #respuesta: 30515
#print("Si pagas 30515 Americus es porque gastaste:", americusToCwh(30515))		 #respuesta: 10123

# tiempo_inicial = time() 
main()
# tiempo_final = time() 
 
# tiempo_ejecucion = tiempo_final - tiempo_inicial
 
# print ('El tiempo de ejecucion fue:',tiempo_ejecucion) #En segundos