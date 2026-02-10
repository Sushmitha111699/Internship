class Student:
    college_name = "MRIT College"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    @classmethod
    def change_college(cls, new_name):
        cls.college_name = new_name
    @staticmethod
    def is_pass(marks):
        if marks >= 35:
            return "Pass"
        else:
            return "Fail"
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("College:", Student.college_name)
s1 = Student("Sushmita", 101)
s2 = Student("Sahitya", 102)
s1.display()
print("Result:", Student.is_pass(78))
print()
s2.display()
print("Result:", Student.is_pass(30))
print()
Student.change_college("MRIT College")
s1.display()
print()
s2.display()
