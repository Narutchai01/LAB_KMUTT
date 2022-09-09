# ข้อที่1 
Jlist = ['Jeff','Jake' ,'Jim']
name = str(input("What is your name? :"))
name = name.capitalize()


def checkJ_name(name):
    if name in Jlist:
        myjList = "Hello, {}. Good morning my firend!"
        return myjList.format(name)
    else:
        print("Who are you")
        notmyjList = "Nice to meet you anyway ...{} :)"
        return notmyjList.format(name)

print(checkJ_name(name))

# ข้อที่ 2 

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

# ข้อที่3
number = int(input("enter a number test:"))

flag = False


def primenumber(n):
    if n > 1:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

primenumber(number)
if flag:
        print("is not a prime number")
else:
        print("is a prime number")


# ข้อที่ 4
element = int(input("your Element :"))

Elist = []


def createList (element): 
    for x in range(element):
        member = int(input())
        Elist.append(member)
    

    
createList(element)
print("The maximim number entered is",max(Elist))
print("The minimim number entered is",min(Elist))


# ข้อที่ 5

print("Please enter a choice for your selection:")
print("Enter 1 if you want to calulate the area of a triangle.")
print("Enter 2 if you want to calulate the volumn of cubic.")
print("Enter 3 if you want to calulate the volumn of cone.")

choice = int(input("Enter your choice here:"))

def areaCalculator():
    base = int(input("Please the base length :"))
    height = int(input("Please the height :"))
    s = 1/2 * base * height
    result = "The are of triangle with base = {} and height = {} is {} "
    return result.format(base,height,s)


def cubiccalculator():
    base = int(input("Please the base width :"))
    length = int(input("Please the length :"))
    height = int(input("Please the height :"))
    cubic = base * length * height
    result = "The cubic volum of width = {} length = {} and height = {} is {}"
    return result.format(base,length,height,cubic)

def coniccalculator():
    base = int(input("Please the base diameter :"))
    height = int(input("Please the height :"))
    r = base/2
    conic = (((r**2)*22/7)*height)/3
    result = "The conical volumn of cone with daimeter = {:.1f} and hegiht = {:.1f} is {:.12f}"
    return result.format(base,height,conic)

if choice == 1:
    print(areaCalculator())
elif choice == 2:
    print(cubiccalculator())
elif choice == 3:
    print(coniccalculator())
else:
    print("Invalid Choice")