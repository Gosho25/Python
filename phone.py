class Phone: #22205
    def __init__(self, brand, model, price, color, manufacture_year):
        self.brand = brand                  
        self.model = model                  
        self.price = price                  
        self.color = color                
        self.manufacture_year = manufacture_year  

    def calculate_discount(self):
        if 2015 <= self.manufacture_year <= 2021:
            discount = 0.05  
        elif self.manufacture_year < 2015:
            discount = 0.15  
        else:
            discount = 0.00  
        return self.price * discount

    def discounted_price(self):
        return self.price - self.calculate_discount()

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price:}")
        print(f"Color: {self.color}")
        print(f"Manufacture year: {self.manufacture_year}")
        print(f"Discount: {self.calculate_discount():}")
        print(f"Price after discount: {self.discounted_price():}")
        print("===================")


phone1 = Phone("Samsung", "Galaxy S25", 1200.00, "Black", 2025)
phone2 = Phone("Apple", "iPhone 15", 2800.00, "Purple", 2010)
phone3 = Phone("Xiaomi", "Redmi 10T", 600.00, "White", 2019)


phone1.display_info()
phone2.display_info()
phone3.display_info()