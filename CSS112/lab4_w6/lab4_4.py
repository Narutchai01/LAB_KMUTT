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