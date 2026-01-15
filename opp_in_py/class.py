
# class Student:
#     roll = ""
#     cgpa = ""


# Zim = Student()
# Zim.roll = 101
# Zim.cgpa = 3.54

# Rakib = Student()
# Rakib.roll = 102
# Rakib.cgpa = 3.50
# Rakib.cgpa = 3.50

# print(f"Roll: {Zim.roll} and CGPA: {Zim.cgpa}")
# print(f"Roll: {Rakib.roll} and CGPA: {Rakib.cgpa}")



class Student:
    roll = ""
    cgpa = ""
    name =""

    def __init__(self, roll, cgpa,name):
        self.roll = roll
        self.cgpa = cgpa
        self.name = name

    def display(self):
        print(f"Name:{self.name} Roll: {self.roll} and CGPA: {self.cgpa}")



Zim = Student(name = 'Zim',roll = 101, cgpa = 3.56)
name = Zim.display()

# Kim = Student()
# Kim.set_value(name = "kim", roll = 102, cgpa = 3.50)
# Kim.display()

# Rim = Student()
# Rim.set_value(name = "Rim", roll = 103, cgpa = 3.90)
# Rim.display()

Kim = Student(name = "kim", roll = 102, cgpa = 3.50)
Kim.display()

Rim = Student(name = "Rim", roll = 103, cgpa = 3.90)
Rim.display()