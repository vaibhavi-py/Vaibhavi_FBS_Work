# 2) 

# Base Class
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


# Derived Class
class EnggStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage, branch, internalMarks):
        super().__init__(studentId, name, age, percentage)
        self.branch = branch
        self.internalMarks = internalMarks

    # Accept Method
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))
        self.branch = input("Enter Branch: ")
        self.internalMarks = float(input("Enter Internal Marks: "))

    # Override calculateRank
    def calculateRank(self):
        final_score = (self.percentage * 0.5) + (self.internalMarks * 0.5)

        if final_score >= 90:
            return "Rank 1"
        elif final_score >= 75:
            return "Rank 2"
        elif final_score >= 60:
            return "Rank 3"
        else:
            return "Rank 4"

    # Override __str__
    def __str__(self):
        return (f"Student ID: {self.studentId}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Percentage: {self.percentage}\n"
                f"Branch: {self.branch}\n"
                f"Internal Marks: {self.internalMarks}\n"
                f"Rank: {self.calculateRank()}")

    # Display Method
    def display(self):
        print(self)


# Creating Object
e1 = EnggStudent(101, "Vaibhavi", 21, 85, "Computer", 90)

e1.display()
