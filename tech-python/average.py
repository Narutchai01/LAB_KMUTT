def average(nums): 
    txt = f"The average of {nums} is {sum(nums)/len(nums)}"
    return txt

nums = []
while True: 
    numIN = int(input("Enter an interger (-1 to exit) :"))
    if numIN < 0: 
        break
    nums.append(numIN)

print(average(nums)) 


