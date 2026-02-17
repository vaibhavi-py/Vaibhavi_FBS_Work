# 1) 

class Complex:

    # Constructor
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print("Complex Object Created")

    # Operator Overloading for +
    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        return Complex(r, i)

    # Operator Overloading for -
    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        return Complex(r, i)

    # Display using __str__
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Destructor
    def __del__(self):
        print("Complex Object Destroyed")


# Creating Objects
c1 = Complex(4, 5)
c2 = Complex(2, 3)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)
