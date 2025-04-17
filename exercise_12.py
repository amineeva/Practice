# calculate income tax

income_2025 = 45000

def income_tax(income):
    total_tax = 0;
    if income<10000:
        return 0
    else:
        total_tax += 10000*0
        income = income - 10000
        print(income)
    if income < 10000:
        return total_tax
    else:
        total_tax += 10000*0.1
        income = income - 10000
        print(income)
    if income>0:
        total_tax += income*0.2
        print(income)
    return total_tax

print(income_tax(income_2025))
