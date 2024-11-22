class Number:
    def __init__(self, num1):
        self.num1 = int(num1)
    def show(self):
        print(f"Num1 = {self.num1}")

class Doublenum(Number):
    def __init__(self, num1, num2):
        super().__init__(num1)
        self.num2 = int(num2)
    def show(self):
        print(f"Num1 = {self.num1}\n Num2 = {self.num2}")

Nu = Number(2)
Du = Doublenum(2, 5)
Nu.show()
Du.show()