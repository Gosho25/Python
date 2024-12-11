class Student:
    def __init__(self, name, group, success):
        self.name = name
        self.group = int(group)
        self.success = float(success)
student1 = Student("Ivan", 2, 4.50)
print(student1.name)
print(student1.group)
print(student1.success) 
