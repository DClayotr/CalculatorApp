#Recieves a paresed array from the EqParse function and sends the proper operators to the CalDataType function
#Basically is the logic that will calculate the total of the entire equation

from CalDataType import calculate 
from EqParse import EqParse

def eqIterator(eqArray_temp):

    calculation = False
    index = 0

    eqArray = []
    eqArray = EqParse(eqArray_temp)

    leftNum = 0
    rightNum = 0

    PEMDAS = ['^', '*', '/', '+', '-']

    while index < len(PEMDAS):
 
        
        for i in range(len(eqArray)):
            
            place = eqArray[i]
            
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
print(eqIterator(x))
