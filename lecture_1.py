age: int = 10
print(age)
age = "i do not know"  # error with mypy
print(age) 

numset: set[str] = {'a','b','c'}
numset: set[str] = {'a','b','c',1} # error with mypy

arr: list[int] = [1,2,3,4]
arr2: list[int] = [1,2,3,4,'a'] # error with mypy

vector = list[list[int]]
ll1: vector = [[1,2,3],[4,5,6]]
ll2: vector = [[1,2,3],[4,5,'a']] # error with mypy


