def temperature(start,end): 
    if (start <= end ): 
        res = (start*9/5)+32
        filefour.write(f'{start} degrees Celsius is {res:.2f} degrees Fahrenheit\n')
        temperature(start+1,end)
    

start = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter an ending Celcius value: "))
filefour = open("multiply.txt", 'w') 
temperature(start,end)





