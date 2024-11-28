class Building:
    def __init__(self, area, address, height):
        self.area = float(area) 
        self.address = str(address)  
        self.height = int(height)  

    def Output(self):
        print(f"Сграда на адрес {self.address}, височина: {self.height}м, площ: {self.area} кв.м")


class House(Building):
    def __init__(self, area, address, height, floors, owner_name):
        super().__init__(area, address, height)
        self.floors = int(floors)  
        self.owner_name = str(owner_name)  

    def Output(self):
        print(f"Къща на адрес {self.address}, собственик: {self.owner_name}, височина: {self.height}м, площ: {self.area} кв.м, етажи: {self.floors}")

    def average_floor_height(self):
        if self.floors > 0:
            return self.height / self.floors
        return 0  # За случай на 0 етажа (макар че такъв не трябва да се случва)


def find_largest_house(houses):
    max_avg_height = -1  
    largest_house = None  

    for house in houses:
        avg_height = house.average_floor_height()
        if avg_height > max_avg_height:
            max_avg_height = avg_height
            largest_house = house

    return largest_house



house1 = House(200, "ул. Пример 1", 10, 2, "Иван Иванов")
house2 = House(250, "ул. Пример 2", 12, 3, "Мария Георгиева")
house3 = House(150, "ул. Пример 3", 8, 1, "Петър Петров")


houses = [house1, house2, house3]

for house in houses:
    house.Output()

largest_house = find_largest_house(houses)
print("\nНай-просторната къща с най-голяма средна височина на етаж:")
largest_house.Output()  
