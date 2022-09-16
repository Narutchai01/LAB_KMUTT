print("Convert Centimeter into Inch")
print("Convert Kilogram into Pound")
print("Convert Celcius into Fareheit")
print("Convert Litre into US  Gallon")


def Celcius(c):  # แปลงค่าอุณหภูมิ
    f = ((c*9)/5)+32
    return f"the {c:.1f} Celcius(es) equal to {f:.2f} Farenheit "

def Centimeter_function(centi): #แปลงค่าเซน
    Inch = centi/2.54
    return f"The {centi:.1f} Centimeter(s) equal to {Inch:.2f} Inch"


def Pond_function(Gilog): #แปลงกิโลกรัม
    Pound = Gilog*2.2
    return f"The {Gilog:.1f} gilogram(s) equal to {Pound:.2f} Pound"


def Litre_to_USGallon_function(litre): #แปลง litre
    us_gal = litre/3.785
    return f"The {litre:.1f} Litre(s) equal to {us_gal:.2f} Us Gallon"


while True:
        choise = int(input("enter choice(1/2/3/4) : "))

        if choise > 0 and choise < 5:
            if choise == 1:
                while True:
                    centi = float(input("Enter Dimesion in Centimeter :"))
                    print(Centimeter_function(centi))

                    char = str(
                        input("Let's do next calculation? (Y/N) : ")).capitalize()
                    if char == 'Y':
                        True
                        break
                    elif char == 'N':
                        False


            elif choise == 2:
                while True:
                    Gilog = int(input("Enter weight in Killogram :"))
                    print(Pond_function(Gilog))

                    
                    char = str(
                        input("Let's do next calculation? (Y/N) : ")).capitalize()
                    if char == 'Y':
                        True
                        break
                    elif char == 'N':
                        False

            elif choise == 3:
                while True:
                    c = int(input("Enter temperature in Celcius :"))
                    print(Celcius(c))
                    
                    
                    char = str(
                        input("Let's do next calculation? (Y/N) : ")).capitalize()
                    if char == 'Y':
                        True
                        break
                    elif char == 'N':
                        False


            elif choise == 4:

                while True:
                    litre = int(input("Enter Volume in Litre :"))
                    print(Litre_to_USGallon_function(litre))

                
                    char = str(
                        input("Let's do next calculation? (Y/N) : ")).capitalize()
                    if char == 'Y':
                        True
                        break
                    elif char == 'N':
                        False
        else:
            print("Invalid Input")
            

            
