
def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif salary >= 11850 and salary <= 34500:
        return (salary - 11850) * 0.2
    elif salary >= 34501 and salary <= 150000:
        return ((salary - 34500) * 0.4) + 4530 
    else:
        return ((salary - 150000) * 0.45) + 50730 
salary = 15850	 
ta = getIncomeTax(salary)
print(f"Tax amount for salary £{salary} is £{ta}")