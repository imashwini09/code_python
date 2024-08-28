import sys
import gc

gc.set_debug(True)
a = "hello world"
print(sys.getrefcount(a))

mylist = []
mylist.append(a)

print(sys.getrefcount(a))

# print(gc.get_referrers(a))

print(gc.get_threshold())

# gc.set_threshold = (1000,20,30)
print(gc.get_count())
