class Firma: #22205
    def __init__(self, id_num, fname, lname, experience_firma, salary, age):
        self.id_num = id_num          
        self.fname = fname           
        self.lname = lname            
        self.experience_firma = experience_firma  
        self.salary = salary          
        self.age = age                

    def calculate_bonus(self):
        if 5 <= self.experience_firma <= 10:
            bonus = self.salary * 0.015
        elif self.experience_firma > 10:
            bonus = self.salary * 0.02
        else:
            bonus = self.salary * 0.005
        return bonus

    def total_salary(self):
        return self.salary + self.calculate_bonus()

    def display_info(self):
        print(f"ID: {self.id_num}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Experience_firma: {self.experience_firma}")
        print(f"Salary: {self.salary}")
        print(f"Age: {self.age}")
        print(f"Bonus: {self.total_salary():}")
        print("==================================")
def create_employee():
    id_num = input("ID: ")
    fname = input("Fname: ")
    lname = input("Iname: ")
    experience_firma = int(input("Expirience(years): "))
    salary = int(input("Salary: "))
    age = int(input("Age: "))
    return Firma(id_num, fname, lname, experience_firma, salary, age)

employee1 = create_employee()
employee2 = create_employee()

employee1.display_info()
employee2.display_info()  