def EqParse(Equation):

    numSubString = '' #acts as a buffer that holds the value that will be added to the parsed EqArray
    EqArray = [] #holds each part of the equation, either number or operator, in seperat indexes for the program to read

    for i in range(len(Equation)):
        
        EqIndex = Equation[i]

        #If block will set numSubString to a value then wait to recieve the next value before it appends the old one
        #numSubString is then reassigned to the current value held in EqIndex
        #This method prevents repetative checking

        if(EqIndex.isnumeric()):
            if(numSubString == '' or numSubString.isnumeric()):
                numSubString = numSubString + EqIndex
            else:
                EqArray.append(numSubString)
                numSubString = EqIndex

        elif(EqIndex == '+' and (numSubString.isnumeric() or numSubString == ')' or numSubString == '(')):
            if(numSubString.isnumeric()):
                EqArray.append(int(numSubString))
                numSubString = '+'
            else:
                EqArray.append(numSubString)
                numSubString = '+'
            
        elif(EqIndex == '-' and (numSubString.isnumeric() or numSubString == ')' or numSubString == '(')):
            if(numSubString.isnumeric()):
                EqArray.append(int(numSubString))
                numSubString = '-'
            else:
                EqArray.append(numSubString)
                numSubString = '-'

        elif(EqIndex == '*' and (numSubString.isnumeric() or numSubString == ')' or numSubString == '(')):
            if(numSubString.isnumeric()):
                EqArray.append(int(numSubString))
                numSubString = '*'
            else:
                EqArray.append(numSubString)
                numSubString = '*'

        elif(EqIndex == '/' and (numSubString.isnumeric() or numSubString == ')' or numSubString == '(')):
            if(numSubString.isnumeric()):
                EqArray.append(int(numSubString))
                numSubString = '/'
            else:
                EqArray.append(numSubString)
                numSubString = '/'

        elif(EqIndex == '('):
            if(numSubString.isnumeric()):    
                EqArray.append(int(numSubString))
                numSubString = '('
            else:
                EqArray.append(numSubString)
                numSubString = '('

        elif(EqIndex == ')'):
            if(numSubString.isnumeric()):    
                EqArray.append(int(numSubString))
                numSubString = ')'
            else:
                EqArray.append(numSubString)
                numSubString = ')'
            
        else:
            continue

    if(numSubString.isnumeric() or numSubString == ')'): #appends the last value in the given equation, will not append if the value is non-numeric
        if(numSubString.isnumeric()):    
            EqArray.append(int(numSubString))
        else:
            EqArray.append(numSubString)
    else:
        pass

    return EqArray

EqParse("716565/(82156+6554+2222)")