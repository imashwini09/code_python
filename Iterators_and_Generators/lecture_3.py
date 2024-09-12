# Generators


def my_generator():
    for i in range(500000):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))