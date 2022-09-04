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
