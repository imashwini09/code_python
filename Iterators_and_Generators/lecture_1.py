# it is an object that allows you traverse from element of collection one at a time
# __iter__() return object of iterator
# __next__()

arr = [1,2,3,4,5]
iterator = iter(arr)

print(next(iterator))
print(next(iterator))


for i in iterator:
    print(i)

    
