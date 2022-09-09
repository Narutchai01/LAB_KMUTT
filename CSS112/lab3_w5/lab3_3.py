number = int(input("enter a number test:"))

flag = False


def primenumber(n):
    if n > 1:
        # check for factors
        for i in range(2, n):
            if (n % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

primenumber(number)
if flag:
        print("is not a prime number")
else:
        print("is a prime number")
