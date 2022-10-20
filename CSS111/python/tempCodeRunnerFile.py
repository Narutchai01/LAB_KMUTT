number = input("enter a number: ")

def func(number):
    number = [int(i) for i in number]
    for i in range(len(number)-1):
        if i % 2 == 0:
            if number[i] >= number[i+1]:
                return False
        else:
            if number[i] <= number[i+1]:
                return False
    else:
        return True

        
print(func(number))