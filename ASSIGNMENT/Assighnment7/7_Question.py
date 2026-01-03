# TWO MERGE TRIANGLE PATTERNS.

n = 5

for i in range(1, n + 1):
    # left triangle
    print("*" * i, end="")
    
    # spaces in the middle
    print(" " * (2 * (n - i)), end="")
    
    # right triangle
    print("*" * i)
