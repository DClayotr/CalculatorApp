
#leftNum and RightNum represent the numbers on the left and right of the operating symbol in the given substring of the equation
#opSymble holds a mathimatical operater character (+-*/) and is check to perform an operation on left and right Num
#calculate sets and returns the value of total

def calculate(opSymble, leftNum, rightNum):

    total = 0
    operand = opSymble.strip()

    if(operand == '+'):

        total = leftNum + rightNum

    elif(operand == '-'):

        total = leftNum - rightNum

    elif(operand == '*'):

        total = leftNum * rightNum

    elif(operand == '/'):

        total = leftNum / rightNum

    else:
        exit(0)


    return total

