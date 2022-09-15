def fibonacci(i):
    if i == 0:
        return i
    elif i == 1:
        return i 
    else:
        return fibonacci(i-1)+(fibonacci(i-2))
for i in range(5):
    print(fibonacci(i))