class Arithmetic:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def values(self):
        print(f"a: {self.a}, b: {self.b}")
    def sum(self):
        return self.a -self.b
    def difference(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        if self.b != 0:
            return self.a / self.b
        else:
            print("b can not be 0")

a = float(input("a = "))
b = float(input("b = "))
arithmetic = Arithmetic(a, b)
print(f"Sum = {arithmetic.sum()}")
print(f"Difference = {arithmetic.difference()}")
print(f"Multiplication = {arithmetic.multiplication()}")
print(f"Division = {arithmetic.division()}")