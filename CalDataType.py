class OperationTree(): #Data structure that takes two numbers as 'right' and 'left' and an additional operator symbol '+,-.*,/' 

    def __init__(self, symble, leftNum, rightNum): #defines 
        self.opSymble = symble
        self.leftNum = leftNum
        self.rightNum = rightNum

    def calculate(self):

        total = 0
        operand = self.opSymble.strip()

        if(operand == '+'):

            total = self.leftNum + self.rightNum

        elif(operand == '-'):

            total = self.leftNum - self.rightNum

        elif(operand == '*'):

            total = self.leftNum * self.rightNum

        elif(operand == '/'):

            total = self.leftNum / self.rightNum

        else:
            exit(0)


        return total
