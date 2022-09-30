filetwo  = open('myFile.txt', 'r')

def numalphbet():
    data = len(filetwo.read())
    return f'Total letters are {data}'


print(numalphbet())
