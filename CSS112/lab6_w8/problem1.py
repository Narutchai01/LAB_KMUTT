def p1():
    x=input().split()
    c=input()
    #Your code here
    ans = [i.count(c) for i in x]
    #End Your Code
    print(*ans)
