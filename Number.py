class Number:
    def __init__(self, n1):
        self.n1 = n1

    def __mul__(self, new):
        return Number(self.n1 * new.n1)
    

num1 = Number(5)
num2 = Number(8)
result = num1 * num2
print(result.n1, ) 