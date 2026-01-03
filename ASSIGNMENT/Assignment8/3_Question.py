## sum of all odd number between 1 to n .

def sum_of_odds(n):
    return sum(range(1, n + 1, 2))

n = int(input("Enter a number: "))
print("Sum of all odd numbers from 1 to", n, "is:", sum_of_odds(n))
