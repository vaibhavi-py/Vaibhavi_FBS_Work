# 3) 

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
class MedicalStudent(Student):

    # Parameterized Constructor
    def __init__(self, studentId, name, age, percentage, specialization, marksOfInternship):
        super().__init__(studentId, name, age, percentage)
        self.specialization = specialization
        self.marksOfInternship = marksOfInternship

    # Accept Method
    def accept(self):
        self.studentId = int(input("Enter Student ID: "))
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.percentage = float(input("Enter Percentage: "))
        self.specialization = input("Enter Specialization: ")
        self.marksOfInternship = float(input("Enter Internship Marks: "))

    # Override calculateRank
    def calculateRank(self):
        final_score = (self.percentage * 0.5) + (self.marksOfInternship * 0.5)

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
                f"Specialization: {self.specialization}\n"
                f"Internship Marks: {self.marksOfInternship}\n"
                f"Rank: {self.calculateRank()}")

    # Display Method
    def display(self):
        print(self)


# Creating Object
m1 = MedicalStudent(201, "Vaibhavi", 22, 88, "Cardiology", 92)

m1.display()
