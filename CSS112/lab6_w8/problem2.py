def p2():
   posneg = [ int(i) for i in input().split()]
   noneg = [i for i in posneg if i >= 0]#Your code here
   print(*noneg)

