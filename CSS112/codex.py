alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# number = int(input("Enter a number: "))
alist = []
lit = []
def endcoding():
    for i in word:
        if i in alphabet:
            index = alphabet.index(i)
            index = index + number
            if index > 25:
                index = index - 26
            alist.append(alphabet[index])
        else:
            alist.append(i)
    print("".join(alist))

def decoding():
    for i in word:
        if i in alphabet:
            index = alphabet.index(i)
            index = index - number
            if index < 0:
                index = index + 26
            lit.append(alphabet[index])
        else:
            lit.append(i)
    print("".join(lit))


print('pless enter "A" for endcoding or "B" for decoding')
alpha = str(input("Enter a alphabet: ")).upper()
# number = int(input("Enter a number: "))
word = input("Enter a word: ")
word = word.upper()

if alpha == "A":
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            endcoding()
            break
        else:
            print('error')
elif alpha == "B":
    while True:
        number = int(input("Enter a number: "))
        if number > 0:
            decoding()
            break
        else:
            print('error')
else:
    print('error')
