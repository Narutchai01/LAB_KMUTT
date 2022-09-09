base = int(input("Please the base diameter :"))
height = int(input("Please the height :"))
r = base/2
r*=r
conic = ((r*3.14)*height)/3
result = "The conical volumn of cone with daimeter = {:.2f} and hegiht = {} is {}"
print(result.format(base,height,conic))
