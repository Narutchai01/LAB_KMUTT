knum = list(range(-5,5))

evenlist = list(filter(lambda x: x % 2 == 0, knum))
oddlist = list(filter(lambda x: x % 2 != 0, knum))

print(evenlist)
print(oddlist)