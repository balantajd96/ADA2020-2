## Juan Diego Balanta
## id: 0220859
## 21 de Octubre de 2020
##
## Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali me comprometo
## a seguir los más altos estándares de integridad académica.
from sys import stdin
#shortStick representa el valor mas pequeño que voy a armar
#currentStick representa el palo que estoy armando para obtener shortStick
#usedStick es el palo que voy a agregarle a current stick
def solve(shortStick, usedStick,currentStick):
    global sticks
    # print("los palos cortados fueron")
    # print(sticks)
    # print("el palo más corto es:", shortStick)
    newStick=usedStick+currentStick
    for i in range(len(sticks):
        if len(sticks)==0 and (shortStick==currentStick):
            return shortStick
        else:
            if len(sticks)!=0 and shortStick> newStick:
                ##### agregar otro palo
                pass
            
            if len(sticks)!=0 and shortStick==currentStick:
                #si ya arme un palo y me falta por armar entonces debo armar otro desde 0
                solve(shortStick,sticks[i]+1,0)
        
    
def solves(shortStick, usedStick,currentStick):
    print("el caso es: ",shortStick,usedStick,currentStick)
    

def main():
    global sticks
    line=int(stdin.readline())
    while(line!=0):
        sticks = [ int(x) for x in stdin.readline().split() ]
        sticks.sort(reverse=True)
        bigStick=sticks.sum()
        shortStick,i=sticks[0],0
        while((bigStick/2)>=shortStick):        
            if(bigStick%shortStick==0):
                if(solves(i ,0,0))
                   return i 
            i+=1
            shortStick=sticks[i]
            
        line=int(stdin.readline())
print(main())