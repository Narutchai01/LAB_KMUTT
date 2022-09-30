filethree = open('myFile.txt', 'r')

def main():
    data = filethree.read()

    x = data.split()

    return f'Total words are {len(x)}'

print(main())