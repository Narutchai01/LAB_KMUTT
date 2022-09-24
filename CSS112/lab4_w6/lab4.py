# ข้อที่1

def fullname():
    def callname():
        name = input("Please enter your name: ")
        surname = input("Please enter your surname: ") 
        fname = name + " " + surname 
        return fname
    
    
    return f"Hi, {callname()}" 


print(fullname())
        

# ข้อที่2 
def temperature(start,end): 
    if (start <= end ): 
        res = (start*9/5)+32
        print (f'{start} degrees Celsius is {res:.2f} degrees Fahrenheit')
        temperature(start+1,end)
    

start = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter an ending Celcius value: "))
temperature(start,end)

# ข้อที่3
def multiply(a, b):
    if b<=12: 
        print(f"{a} x {b} = {a*b}")
        multiply(a,b+1)


num = int(input("Enter a number: ")) 
print("Multiplication table for",num) 
multiply(num, 1)

# ข้อที่4
name = input("Please enter your name: ").capitalize()
age = int(input("please enter your age: ")) 

def checkTicket(name, age):
    priceout = 0 
    
    def checkVIP(name): 
        vip = ["Tony","Peter","Mark","Kim","James","Kenny"]
        if name in vip: 
            x = True
            return x 
        else:
            x = False
            return x 
    
    if checkVIP(name) == True: 
        if age < 15: 
            priceout = 3.75
            return f"Tiket price for {name} is $ {priceout:.2f}"
        else: 
            priceout = 7.5
            return f"Tiket price for {name} is $ {priceout:.1f}"
    else: 
        if age < 15: 
            priceout = 7.5 
            return f"Tiket price for {name} is $ {priceout:.1f}"
        else: 
            priceout = 15.0
            return f"Tiket price for {name} is $ {priceout:.1f}"
            
    
    
    
print(checkTicket(name, age)) 