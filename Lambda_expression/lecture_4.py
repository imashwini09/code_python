arr = [1,2,3,4,5]

square = list(filter(lambda x:x%2 == 0, arr))
square1 = list(map(lambda x:x%2 == 0, arr))


print(square)
print(square1)

