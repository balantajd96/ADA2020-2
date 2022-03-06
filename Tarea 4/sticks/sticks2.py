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