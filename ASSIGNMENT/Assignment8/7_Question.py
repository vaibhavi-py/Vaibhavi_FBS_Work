## WAP TO FIND REVERSE OF NUMBER USING FUNCTION.

def revNum(num, rev = 0):
    if(num==0):
        return rev
    else:
        return revNum(num//10 , rev * 10 + num%10)


num = 368 
rev_num = revNum(num)
print(rev_num)
