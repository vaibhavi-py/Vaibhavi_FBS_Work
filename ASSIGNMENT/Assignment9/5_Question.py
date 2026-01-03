# WAP TO FIND FACTORIAL USING RECURSIVE FUNCTION .

def fact(n):
    if(n==0):
        return 1
    else:
        return n * fact(n-1)

n = 5
res = fact(n)
print(res)
