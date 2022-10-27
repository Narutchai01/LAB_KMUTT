numlist = list(range(20))

print(numlist)
evenlist = list(i for i in range(len(numlist)) if numlist[i] %2 ==0)
print("your even number list",evenlist)