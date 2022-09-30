# 1 
def checkword():
    try: 
        fileone = open('myFile.txt','r')
    except:
        return 'Unable to open file myFile.txt'
    else:
        result = fileone.read()
        return f'{result} \nSuccessfully print content in myFile.txt'
    fileone.close()


print(checkword())

# 2
filetwo  = open('myFile.txt', 'r')

def numalphbet():
    data = len(filetwo.read())
    return(data)


print(numalphbet())

# 3

filethree = open('myFile.txt', 'r')

def main():
    data = filethree.read()

    x = data.split()

    return len(x)

print(main())

# 4
def temperature(start,end): 
    if (start <= end ): 
        res = (start*9/5)+32
        filefour.write(f'{start} degrees Celsius is {res:.2f} degrees Fahrenheit\n')
        temperature(start+1,end)
    

start = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter an ending Celcius value: "))
filefour = open("temperature.txt", 'w') 
temperature(start,end)





