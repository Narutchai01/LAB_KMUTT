def fullname():
    def callname():
        name = input("Please enter your name: ")
        surname = input("Please enter your surname: ") 
        fname = name + " " + surname 
        return fname
    
    
    return f"Hi, {callname()}" 


print(fullname())
        