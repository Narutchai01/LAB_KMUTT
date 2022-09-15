print("[A] = Shampoo : 30 bath")
print("[B] = Soap : 20 bath")
print("[C] = Cream : 40 bath")

quint = int(input("How many product do you choose"))
for i in range (quint):
    Choose = str(input("Choose your product {} : ".format(i)))
    Num = int(input("How many?:"))
    if Choose == "A":
        Total = total+(Num*30)
    elif Choose == "B":
        Total = otal+(Num*30)
    elif Choose == "C":
        Total = Total+(Num*30)
    else:
        print("Sorry, we don't have that")
print("Total:" ,Total)
