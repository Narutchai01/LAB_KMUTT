num = [int(i) for i in input().split()]

numlist = list(filter(lambda x: int(x) >= 0 , num))

print(numlist)