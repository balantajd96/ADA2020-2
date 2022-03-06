## Juan Diego Balanta
## id: 0220859
## 10 de Octubre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.

from sys import stdin
global codes,firstHund

def solve(numberToCode,stringObtained):
    #Backtracking
    global codes, firstHund
    if firstHund<100:#Solo queremos imprimir los primeros 100 elementos o "contrasenias"
        if len(numberToCode)==0:
            #en caso de que no tengamos que codificar imprimimos la cadena completa ya encriptada
            print(stringObtained)
            #al imprimir una solucion debo contarla como una solucion entre las 100 primeras
            firstHund+=1
        else:
            #en caso de que tenga que seguir buscando o tenga un codigo por encriptar
            #obtengo la llave a tener en cuenta para encriptar
            key=int(numberToCode[0])
            if key==0:
                #si la llave es un 0 debor revisar si es un 0 que precede,
                # por ende buscamos que hayan al menos dos elementos o caracteres en la clave
                # para que ese 0 se cuente como un precesor 
                if len(numberToCode)>1:
                    #de ser asi, debemos eliminar ese 0 pero no cambiamos la cadena
                    solve(numberToCode[1:],stringObtained)
            else:
                #de lo contrario debemos revisar con que vamos a encriptar la clave
                # revisamos el diccionario de claves en options 
                options=codes[key]
                for codigo in options:
                    #number corresponde al valor numerico de la clave, y letra es 
                    # el caracter por el que se va a reemplazar number en la clave "numberToCode"
                    number,letra=codigo
                    if len(number)==1:
                        #de ser un valor de 1 a 9 eliminamos el primer elemento de numberToCode
                        # y agregamos esa letra a la cadena que llevamos hasta ahora 
                        solve(numberToCode[1:],stringObtained+letra)
                    else:
                        #de ser un valor de 10 en adelante al que vaya a codificar, tenemos entonces 
                        # que revisar que el valor de la unidad en el diccionario sea igual al de la clave numberToCode 
                        if (len(numberToCode)>1) and (numberToCode[1]==number[1]):
                            #si obtengo ese valor en la clave entonces mando numberToCode sin esos dos elementos iniciales
                            # y a la cadena le agrego el valor correspondiente del diccionario 
                            solve(numberToCode[2:],stringObtained+letra)

def main():
    global codes,firstHund
    test=int(stdin.readline())
    cases=1
    while(test!=0):
        #codes representa el agrupamiento de los valores de 1 a 99
        # quines se agrupan segun su primer valor, ejemplo
        # los valores de 1,10 - 19 se encuentran en el diccionario 1
        # los valores de 2,20 - 29 se encuentran en el diccionario 2
        #y asi sucesivamente, estos tambien se organizan en orden alfabetico
        # asi que a 12 estaría primero que c 1 en la llave 1
        codes={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
        firstHund=0
        for i in range(test):
            tok = stdin.readline().split()
            key=int(tok[1][0])
            codes[key].append((tok[1],tok[0]))
        encription=stdin.readline().strip()
        for i in codes:
            codes[i].sort(key=lambda x:x[1])
        print("Case #{casos}".format(casos=cases))
        ##
        ##debo mandarle la llave a encriptar completa, y una cadena vacia para ir agregando las "encriptaciones"
        ##
        solve(encription,'')
        #print("Codigos:",codes,"clave a encriptar:",encription)
        cases+=1
        if firstHund==0:    
            print("")
        print("")
        test=int(stdin.readline())


main()