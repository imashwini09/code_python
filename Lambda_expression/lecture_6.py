from functools import reduce

words = ["hello", " ", "world"]

conc = reduce(lambda x,y : x+y, list(filter(lambda word: word!=" ", words)))

print(conc)