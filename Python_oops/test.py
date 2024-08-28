import array
arr = array.array('i',[1,2,3])

arr.append(4)
for i in arr:
        print(i,end= " ")
# Array of signed chars
print()
arr_b = array.array('b', [1, 2, 3])
print(arr_b)

# Array of unsigned chars
arr_B = array.array('B', [1, 2, 3])
print(arr_B)

# Array of Unicode characters
arr_u = array.array('u', 'hello')
print(arr_u)

# Array of signed shorts
arr_h = array.array('h', [1, 2, 3])
print(arr_h)

# Array of unsigned shorts
arr_H = array.array('H', [1, 2, 3])
print(arr_H)

# Array of signed longs
arr_l = array.array('l', [1, 2, 3])
print(arr_l)

# Array of unsigned longs
arr_L = array.array('L', [1, 2, 3])
print(arr_L)

# Array of floats
arr_f = array.array('f', [1.0, 2.0, 3.0])
print(arr_f)

# Array of doubles
arr_d = array.array('d', [1.0, 2.0, 3])
print(arr_d)

