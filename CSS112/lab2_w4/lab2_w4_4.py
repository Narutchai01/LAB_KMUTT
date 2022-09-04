gard = int(input("Please enter your scande:"))

if gard >= 80:
    print("you gard A")
elif gard >=75 and gard <= 79:
    print("you gard B+")
elif gard >=70 and gard <= 74:
    print("you gard B")
elif gard >=65 and gard <= 69:
    print("you gard C+")
elif gard >=60 and gard <= 64:
    print("you gard C")
elif( gard >=55) and (gard <= 59):
    print("you gard D+")
elif gard >=50 and gard <=54:
    print("you gard D")
else:
    print(" your gard F")