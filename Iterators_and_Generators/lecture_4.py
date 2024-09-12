def fib_generator():
    a,b = 0,1
    while True:
        yield a
        a,b  = b, a+b

gen = fib_generator()

for _ in range(10):
    print(next(gen))

for _ in range(10):
    print(next(gen))