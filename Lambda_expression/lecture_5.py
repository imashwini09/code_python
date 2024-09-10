from functools import reduce
arr = [1,2,3,4,5]

total = reduce(lambda x,y: x+y, arr)

print(total)

mx = reduce(lambda x,y: max(x,y), arr)
print(mx)

