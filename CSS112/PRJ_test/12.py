from functools import reduce

numlist = list(range(10))

num  = list(reduce(lambda x,y: str(x)+str(y),numlist))

print(num)