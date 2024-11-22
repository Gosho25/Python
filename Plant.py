class Plant:
    def __init__(self, name, specis):
        self.name = name
        self.specis = specis

    def Print(self):
        return f"Name: {self.name}, Specis: {self.specis}"


class Flowers(Plant):
    def __init__(self, name, residence,):
        super().__init__(name, "Flowers")
        self.residence = residence

    def Print(self):
        print(f"{super().Print()} Residence: {self.residence}")    

class Vegetables(Plant):
    def __init__(self, name, residence,):
        super().__init__(name, "Vegetables")
        self.residence = residence

    def Print(self):
        print(f"{super().Print()} Residence: {self.residence}")  

class Trees(Plant):
    def __init__(self, name, residence,):
        super().__init__(name, "Trees")
        self.residence = residence

    def Print(self):
        print(f"{super().Print()} Residence: {self.residence}")  


flower = Flowers("Лилия", "Градината")
vegetable = Vegetables("Краставица", "Овощната градина")
tree = Trees("Дъб", "Лесопарк")


flower.Print()
vegetable.Print()
tree.Print()