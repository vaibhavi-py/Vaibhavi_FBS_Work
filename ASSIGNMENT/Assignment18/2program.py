# 2) 

class Distance:

    # Constructor
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
        print("Distance Object Created")

    # Operator Overloading for +
    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm

        # Convert cm to m if >= 100
        if cm >= 100:
            m += cm // 100
            cm = cm % 100

        # Convert m to km if >= 1000
        if m >= 1000:
            km += m // 1000
            m = m % 1000

        return Distance(km, m, cm)

    # Operator Overloading for -
    def __sub__(self, other):
        total_cm1 = (self.km * 100000) + (self.m * 100) + self.cm
        total_cm2 = (other.km * 100000) + (other.m * 100) + other.cm

        result_cm = total_cm1 - total_cm2

        km = result_cm // 100000
        result_cm %= 100000

        m = result_cm // 100
        cm = result_cm % 100

        return Distance(km, m, cm)

    # Display
    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"

    # Destructor
    def __del__(self):
        print("Distance Object Destroyed")


# Creating Objects
d1 = Distance(2, 500, 80)
d2 = Distance(1, 600, 50)

# Addition
d3 = d1 + d2
print("Addition:", d3)

# Subtraction
d4 = d1 - d2
print("Subtraction:", d4)
