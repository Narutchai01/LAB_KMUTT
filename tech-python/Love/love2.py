hour = int(input("Enter hour"))
if hour > 3:
    pay = (hour-3)*30
    print(pay)
else:
    print("free")