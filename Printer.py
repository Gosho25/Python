class Printer:
    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def display(self):
        return f"Name: {self.name}, Price: {self.price}, Year: {self.year}"

    def calculate_sale_price(self):
        if self.year < 2020:
            return self.price * 0.75  
        return self.price


class OilPrinter(Printer):
    def __init__(self, name, price, year, color):
        super().__init__(name, price, year)
        self.color = color

    def display(self):
        print(f"{super().display()}, Color: {self.color}")


class LazerPrinter(Printer):
    def __init__(self, name, price, year, color):
        super().__init__(name, price, year)
        self.color = color

    def display(self):
        print(f"{super().display()}, Color: {self.color}")


oil_printer = OilPrinter("OilAmerican", 150.0, 2018, "Red-Blue")
lazer_printer = LazerPrinter("Future", 200.0, 2021, "Grey")


oil_printer.display()
print(f"Sale Price: {oil_printer.calculate_sale_price()}")

lazer_printer.display()
print(f"Sale Price: {lazer_printer.calculate_sale_price()}")
