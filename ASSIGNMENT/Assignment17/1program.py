# 1)


# PARAMETERIZED CONSTRUCTOR

class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage


s1 = Student(1, "Vaibhavi", 20, 85)
print("Object Created Successfully")



# DISPLAY METHOD

class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("-------------------------")


s1 = Student(2, "Riya", 19, 90)
s1.display()



# ACCEPT METHOD (takinf input from user) 

class Student:

    def __init__(self):
        self.studentId = 0
        self.name = ""
        self.age = 0
        self.percentage = 0

    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))

    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("-------------------------")


s1 = Student()
s1.accept()
s1.display()



# CALCULATE RANK METHOD

class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 90:
            return "Rank 1"
        elif self.percentage >= 75:
            return "Rank 2"
        elif self.percentage >= 60:
            return "Rank 3"
        else:
            return "Rank 4"

    def display(self):
        print("Student ID:", self.studentId)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Percentage:", self.percentage)
        print("Rank:", self.calculateRank())
        print("-------------------------")


s1 = Student(3, "Anjali", 21, 88)
s1.display()



# OVERRIDING __str__

class Student:

    def __init__(self, studentId, name, age, percentage):
        self.studentId = studentId
        self.name = name
        self.age = age
        self.percentage = percentage

    def calculateRank(self):
        if self.percentage >= 90:
            return "Rank 1"
        elif self.percentage >= 75:
            return "Rank 2"
        elif self.percentage >= 60:
            return "Rank 3"
        else:
            return "Rank 4"

    def __str__(self):
        return (f"Student ID: {self.studentId}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Percentage: {self.percentage}\n"
                f"Rank: {self.calculateRank()}")


s1 = Student(4, "Priya", 20, 92)

print(s1)   # __str__ gets called automatically
