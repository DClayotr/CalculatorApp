#Recieves a paresed array from the EqParse function and sends the proper operators to the CalDataType function
#Basically is the logic that will calculate the total of the entire equation

from CalDataType import calculate 
from EqParse import EqParse

def eqIterator(eqArray):

    

    calculation = False
    index = 0
 
    leftNum = 0
    rightNum = 0

    PEMDAS = ['(','^', '*', '/', '+', '-']

    while index < len(PEMDAS):
 
        
        for i in range(len(eqArray)-1):
            
            place = eqArray[i]
            print(place)

            if (place == '('):
                last_closing = len(eqArray) - 1 - eqArray[::-1].index(')')
                recur_list = eqArray[i+1:last_closing]
                eqArray[i] = eqIterator(recur_list)
                del eqArray[i+1:last_closing+1]
                break


            else:
                if(place == PEMDAS[index]):
                
                    leftNum = eqArray[i-1]
                    rightNum = eqArray[i+1]
                    eqArray[i] = calculate(place, leftNum, rightNum)

                    eqArray.pop(i-1)
                    eqArray.pop(i)

                    calculation = True
                    break
                
                else:
                    continue

        if(calculation == True):
            calculation = False
            continue
        else:
            index += 1
            calculation = False
        


    return eqArray[0]        
                
        

x = str(input("Please enter an expression to be evaluated.\n> "))
print(eqIterator(EqParse(x.strip())))
