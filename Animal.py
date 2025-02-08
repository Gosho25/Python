class Animal:
    def __init__(self, name, species):
        self.name = name 
        self.species = species 
  
    def display(self): 
        return f"Name: {self.name}, Species: {self.species}"


class Tiger(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Tiger")
        self.breed = breed

    def display(self):#this is method(NOT function :))))) )
        print(f"{super().display()}, Breed: {self.breed}")


class Elephant(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Elephant")
        self.breed = breed
 
    def display(self):
        print(f"{super().display()}, Breed: {self.breed}")

tiger = Tiger("Sher Khan", "Bengal")
elephant = Elephant("Dumbo", "African")

tiger.display()
elephant.display() 
