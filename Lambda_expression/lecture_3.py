arr = [1,2,3,4,5]

square = list(map(lambda x:x**2, arr))

square1 = list(lambda x: x**2 for x in arr)

square2 = list(x**2 for x in arr)

print(square)
print(square1)
print(square2)