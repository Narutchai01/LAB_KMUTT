numberlist = []


while True:
    num = int(input("enter your number: "))
    if num <= 0:
        break
    numberlist.append(num)
1
def average():
    for i in range(len(numberlist)):
        total = numberlist[i]
        total = (total + total + numberlist[i])/len(numberlist)
        i+=1
        # print(total)

    return f"{total:.2f}"



print(average())