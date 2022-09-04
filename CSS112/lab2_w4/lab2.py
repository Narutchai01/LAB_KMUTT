# ข้อที่ 1
c = int(input("Please enter the temperature in Celsius:"));print("The",float(c),"Celcius =",float((9*c/5)+32),"Farenhite")

# ข้อที่ 2

number = int(input("enter yuor number:"))

i=1
x=0

while i <= number:
    x += i
    i = i+1

print(x)

# ข้อที่ 3 
num = int(input("Enter a number to to make a multiplication table:"))
n=1

while n <= 12:
    print(num,"*",n,"=",num*n)
    n+=1

# ข้อที่ 4 

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

# ข้อที่ 5 
num1 = int(input("Please enter a starting number:"))
num2 = int(input("Please enter a endding number:"))

print("Prime numbers between",num1,"and",num2,"are:")
for i in range(num1,num2):
    if i ==1:
        continue
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)

