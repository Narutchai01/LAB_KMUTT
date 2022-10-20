def swapnum(number):
    num_digit = [i for i in number]
    for i in range(len(num_digit)-1):
        if i % 2 ==0 :
            if num_digit[i] >= num_digit[i+1]:
                return False
        else :
            if num_digit[i] <= num_digit[i+1]:
                return False
    else : return True
number = input()
print(swapnum(number))