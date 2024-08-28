# text = '''print("hello")
# for i in range(10):
#     print("Ashwini",i)
#         '''
# exec(text)

from itertools import permutations

p = permutations(['A','B','C','D'])

# print(tuple(p))
for i in tuple(p):
    print(i)