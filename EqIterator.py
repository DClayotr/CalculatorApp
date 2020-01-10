#Recieves a paresed array from the EqParse function and sends the proper operators to the CalDataType function
#Basically is the logic that will calculate the total of the entire equation

from CalDataType import calculate 
from EqParse import EqParse

def eqIterator(eqArray):

    

    calculation = False
    index = 0
    parenCount = 0
 
    leftNum = 0
    rightNum = 0

    PEMDAS = ['(','^', '*', '/', '+', '-']

    while index < len(PEMDAS):
 
        
        for i in range(len(eqArray)):
            
            place = eqArray[i]

            if (place == '('):
                parenCount = parenCount + 1

            elif (place == ')'):
                parenCount = parenCount - 1            
                if(parenCount == 0):
                    first_opening = eqArray.index('(')
                    recur_list = eqArray[first_opening+1:i]
                    eqArray[i] = eqIterator(recur_list)
                    del eqArray[first_opening:i]
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
        
    return float(eqArray[-1])        
                
        

# x = str(input("Please enter an expression to be evaluated.\n> "))
# print(eqIterator(EqParse(x.strip()))) 
#use for test input

