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