class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = int(age)
        self.school = school
    def show(self):
        print(f"Name: {self.name}\n Age: {self.age}\n School: {self.school}")

class Group(Student):
    def __init__(self, name, age, school, group_num, student_num):
        super().__init__(name, age, school)
        self.group_num = group_num
        self.student_num = student_num
    def show(self):
        print(f"Name: {self.name}\n Age: {self.age}\n School: {self.school}\n Group: {self.group_num}\n Stnumber: {self.student_num}")

def main():
    n = int(input("Enter a number  of students  "))
    schools = []

    for i in range(n):
        name = input(f"Student name {i + 1}: ")
        age = int(input(f"student age {i + 1}: "))
        school = input(f"student schools name {i + 1}: ")
        group_num = input(f"student group number {i + 1}: ")
        student_num = i + 1 

        student = Group(name, age, school, group_num, student_num)
        schools.append(student)

    print("\n Info anbout students:")
    for student in schools:
        print(student.show())

    chosen_group = input("\nEnter a group number for which you want to see the students: ")
    print(f"\nInfo about students group {chosen_group}:")
    for student in schools:
        if student.group.num == chosen_group:
            print(student.group_info())


if __name__ == "__main__":
    main()