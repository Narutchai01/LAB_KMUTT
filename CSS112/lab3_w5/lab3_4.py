element = int(input("Enter number of element :"))

Elist = []


def createList (element): 
    for x in range(element):
        member = int(input())
        Elist.append(member)
    

    
createList(element)
print("The maximim number entered is",max(Elist))
print("The minimim number entered is",min(Elist))