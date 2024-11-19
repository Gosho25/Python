class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print(f"Names: {self.name} {self.family}, Age: {self.age}, Nationality: {self.nationality}")

person1 = Person("Dimitar", "Dimitrov", 30, "UK")
person2 = Person("Georgi", "Samokov", 25, "Bulgaria")
person3 = Person("John", "Smith", 40, "USA")


person1.print()
person2.print()
person3.print()
