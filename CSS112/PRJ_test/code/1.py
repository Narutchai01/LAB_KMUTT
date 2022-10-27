li = [0.2, -1000, 33.21, -101.12, 0.01, 212, 0.4, -0.3, -100]
print(list(map(lambda x: x+10000 if x > -0.5 and x < 0.5 else x, li)))

print([li[x]+10000 if li[x] > -0.5 and li[x] < 0.5 else li[x] for x in range(len(li))])

