def checkword():
    try: 
        fileone = open('1myFile.txt','r')
    except:
        return 'Unable to open file myFile.txt'
    else:
        result = fileone.read()
        return f'{result} \nSuccessfully print content in myFile.txt'
    fileone.close()


print(checkword())
