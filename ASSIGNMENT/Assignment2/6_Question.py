## CALCULATE TOTAL SALARY OF EMPLOYEE BASED ON , DA = 10%, TA = 12%, HRA = 15%

basic = float(input('enter basic salary:',))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra

print('DA =', da)
print('TA = ', ta)
print('HRA = ', hra)
print("Total salary =", total_salary)
