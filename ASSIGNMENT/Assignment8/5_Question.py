# WAP TO FIND PRINT THE FOLLOWING FIBONNACI SERIES USING FUNCTIONS :
# 1 1 2 3 5 8 .


def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = 6   # number of terms
fibonacci(n)
