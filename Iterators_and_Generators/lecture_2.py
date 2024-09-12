class my_iterator:

    def __init__(self,start,end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            temp = self.start
            self.start += 1
            return temp
        else:
            raise StopIteration

ite = my_iterator(1,5)
print(next(ite))
for i in ite:
    print(i)