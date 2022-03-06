## Juan Diego Balanta
## id: 0220859
## 16 de Octubre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
from sys import stdin
#import time

####ESTA SOLUCION NO PASA EN LA ARENA
def solve(string, nCells, goal, newState, index, cells):
    global answer
    if index==nCells:   
        #Verifica si el ultimo caracter anexado es correcto
        if string[0]==string[nCells] and string[1]==string[nCells+1]:
            answer=True
            print("reachable")
            print(string)
            return
    else:
             
        if newState[i]==goal[index]:
            if index!=0:    
                    #Debemos verificar si los nuevos bits que vamos a cambiar
                    # no deben de dañar la cadena ya usada anteriormente 
                if string[index]==cells[i][0] and string[index+1]==cells[i][1]:
                    string[index+2]=cells[i][2]
                    print("index!=0, caso",i)
                    print(string)
                    solve(string, nCells, goal, newState, index+1,cells)                    
                else:   
                    #La primera iteracion
                    string[0]=cells[i][0]; string[1]=cells[i][1]; string[2]=cells[i][2]; 
                    print("primera iteracion")
                    print(string)
                    solve(string, nCells, goal, newState, index+1,cells)
            i+=1
####ESTA SOLUCION SI PASA EN LA ARENA
def solve2(string,cells,nCells,goal,index):
        #string es el binario inicial al que se le agrega un 1 o 0
    ans=None
    if index == nCells-1:
        if cells[string[index-1]+string[index]+string[0]]==goal[index] and cells[string[index]+string[0]+string[1]]==goal[0]:
            ans=True
        else:
            ans=False
    else:
        ans=False
        #temp=string+'0'
        #print('string tiene', string, 'index es igual a', index)
        #print(string[(index-1):(index+1)]+'0')
        if cells[string[(index-1):(index+1)]+'0']==goal[index]:
            ans = solve2(string + '0',cells,nCells,goal,index+1)
        if cells[string[(index-1):(index+1)]+'1']==goal[index] and ans == False:
            ans = solve2(string + '1',cells,nCells,goal,index+1)
    return ans

def main():
    #cells = [['0', '0', '0'], ['0', '0', '1'], ['0', '1', '0'], ['0', '1', '1'], ['1', '0', '0'], ['1', '0', '1'], ['1', '1', '0'], ['1', '1', '1']]
    #endOfFile=False
    #j=1
    lines=stdin.readlines()
    for tok in lines:
        answer=False
        tok=tok.split()
        #tok=stdin.readline().split()
        #Leer hasta el final del archivo, cuando sea vacio es porque llegó al final
        #print("\n-----------------Caso",j,"-----------------\n")
        newState,nCells,goal="{:08b}".format(int(tok[0])),int(tok[1]),tok[2]
        cells={"000":newState[0],"001":newState[1],"010":newState[2],"011":newState[3],"100":newState[4],"101":newState[5],"110":newState[6],"111":newState[7]}
        #transformacion en binario de 8 bits para el resultado de la tabla de verdad
        # o New State que representa al identificador del automata
        
        i = 0
        # 00
        # 01
        # 10
        # 11
        while(i < 4 and answer == False):
            string="{:02b}".format(i)
            answer = solve2(string,cells,nCells,goal,1)
            i += 1
        #for i in range(nCells+2): string.append("")
        #solve(string, nCells, goal, newState, 0, cells)
        if answer:print("REACHABLE")
        else:print("GARDEN OF EDEN")
                #j+=1
            #else: endOfFile=True   
#start_time = time.time()
main()
#print("--- %s seconds ---" % (time.time() - start_time))