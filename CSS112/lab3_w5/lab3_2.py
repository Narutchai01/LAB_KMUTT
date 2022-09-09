hours = int(input('how many hours did you work last week?'))
pay_ment = int(input('Whay is your pay rate per hours(between 10-25)'))


def sallarycalculator(hours,pay_ment):
    if hours > 40 :
        ot = hours - 40
        sallary = ((pay_ment*1.5)*ot)+(40*pay_ment)
    
        return sallary 
    else:
        sallary = hours * pay_ment
    return sallary

result = sallarycalculator(hours, pay_ment)

print(result)