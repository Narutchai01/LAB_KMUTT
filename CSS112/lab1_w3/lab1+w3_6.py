tuple1 = ("ab", 78)
tuple2 = (99, "cd")

tuple1,tuple2 = tuple2,tuple1

print("From the original Tuple 1 = ('ab', 78 )\n\tand Tuple2 = (99, 'cd')\nThe newly swapped tuples are:")
print("Tuple 1 = " + str(tuple1))
print("Tuple 2 = " + str(tuple2))