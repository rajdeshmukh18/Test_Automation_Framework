class A:
    num1 = 5

    def __init__(self, num2):
        self.num2 = num2

    def getvalues(self):
        return str(self.num1) + "" + str(self.num2)


x = A(5)
x.num1 = 10
y = A(6)
A.num1 = 11
print(x.getvalues())
print(y.getvalues())
