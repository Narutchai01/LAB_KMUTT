textsomeone=input()
word1=input()
word2=input()

def func(textsomeone,word1,word2): 
    textsomeone = textsomeone.split(" ")
    n = 0
    for i in range(len(textsomeone)): 
        
        if textsomeone[i] == word1:
            textsomeone[i] = word2
            n+=1
        if word1 in textsomeone[i]:
            q = textsomeone[i].find(word1) 
            textsomeone[i] = textsomeone[i][:q] + word2 + textsomeone[i][q+len(word1):]
            n+=1
            
    print(" ".join(textsomeone))
    print(n)     
    
    
    
func(textsomeone,word1,word2)