number = input()

def func(number):
    for i in range(len(number)-1):
            if number[i] >= number[i+1]:
                return False
            elif number[i] <= number[i+1]:
                return True

print(func(number))