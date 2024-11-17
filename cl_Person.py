class Person:
    def __init__(self, name, family, age,nationality):
        self.name = name
        self.family = family
        self.age = int(age)
        self.nationality = str(nationality)
        
person1 = Person("George","Petkov",35, "bulgarian")#def bulgarian
print(person1.name)
print(person1.family)
print(person1.age)
print(person1.nationality)
