class Box:
    def __init__(self, length, width, height):
        self.lenght = float(length)
        self.width = float(width)
        self.height = float(height)


box1 = Box(12.4 , 10, 15)
box2 = Box(21, 14, 20.5)
volume1 = (f"{box1.height*box1.lenght*box1.width}")
volume2 = (f"{box2.height*box2.lenght*box2.width}")
print(f"box1 lenght is  {box1.lenght}")
print(f"box1 width is {box1.width}")
print(f"box1 height is {box1.height}")
print(f"box1 volume is {volume1} cm3")
print("----------")
print(f"box2 lenght is {box2.lenght}")
print(f"box2 width is {box2.width}")
print(f"box2 height is {box2.height}")
print(f"box2 volume is {volume2} cm3")