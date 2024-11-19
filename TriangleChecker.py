class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        if self.a <= 0 and self.b <= 0 and self.c <= 0:
            return "Нищо няма да работи с отрицателни числа!"
        
        if self.a > 0 and self.b > 0 and self.c > 0:
            return "Ура, можете да построите триъгълник!"
        else:
            return "Жалко, но не можете да направите триъгълник от това"
        
try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
except ValueError:
    print("Трябва да въведете само числа!")
else:
    triangle_checker = TriangleChecker(a, b, c)
    print(triangle_checker.is_triangle())