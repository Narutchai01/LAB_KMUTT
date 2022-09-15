
print("welcome to June shop")
print("[A] = shampoo : 30 bath/1")
print("[B] = soop : 20 bath/1")
print("[C] = cream : 40 bath/1")


how_product = int(input("How many product do you choose : "))
choose = str(input("Choose your product : " ))
many = int(input("How many? : "))


choose = choose.capitalize()
if how_product == 1:
    choose == "A"
    many >= 1
    print("Total : ",(many*30))
elif how_product == 2:
    choose == "B"
    many >= 1
    print("Total :",(many*20))
elif how_product == 3:
    choose == "C"
    many >= 1
    print("Total : ",(many*40))
else:
    print("sorry, we don't have that")


