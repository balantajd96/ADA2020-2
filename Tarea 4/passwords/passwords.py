## Juan Diego Balanta
## id: 0220859
## 12 de Octubre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
from sys import stdin
ans=""
def solve(words, rules, index):
	global ans
    #Si necesito recorrer toda la regla entonces tengo que verificar que el indice no sea igual al tamanio de 
    #la regla, es decir cada caracter 0 o # es una regla diferente, tengo que recorrer esa regla en su totalidad
	if index!=len(rules):
		if rules[index]=="#":
			for i in range(len(words)):
				tmp=ans
				ans=ans+words[i]
				solve(words, rules, index+1)
				ans=tmp
		elif(rules[index]=="0"):
			for i in range(10):
				ans=ans+str(i)
				solve(words, rules, index+1)
				ans=ans[0:len(ans)-1]
	else:
		print(ans)

def main():
	global ans
	line=stdin.readline().strip()
	while (len(line))>0:#end of file
		# nWords representa la cantidad de palabras dadas en el "diccionario" (n) dadas en n lineas consecutivas.
		#print("line es:",line)
		nWords = int(line)
		#print("nwords es",nWords)
		#como dice el ejercicio asumimos que la cantidad de palabras del diccionario es 1 a 100
		#if nWords>0 and nWords<100:
			#en dictionary se almacenan las nWords a utilizar
			# en rules se almacenan todas las posibles #0 que hayan. 
		dictionary=[]; rules=[]
		for i in range(nWords):
			tok=stdin.readline().strip()
			dictionary.append(tok)
		nRules = int(stdin.readline())
		for i in range(nRules):
			tok=stdin.readline().strip()
			rules.append(tok)
		#print("--")	
		for i in range(len(rules)):
			print("--")
			solve(dictionary, rules[i], 0)
			
		ans=""
		line=stdin.readline()
			
		
		
		
main()