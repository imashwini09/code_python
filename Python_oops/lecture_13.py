
# loading gc
import gc
 
# get the current collection 
# thresholds as a tuple
# print("Garbage collection thresholds:",
#                     gc.get_threshold())

# collected = gc.collect()
# print("Garbage collector: collected",
#           "%d objects." % collected)
# x = [1, 2, 3]
# y = [4, 5, 6]
# x.append(y)
# y.append(x)
# # Prints Garbage collector 
# collected = gc.collect()

# # as 0 object
# print("Garbage collector: collected",
#           "%d objects." % collected)


i = 0
 
# create a cycle and on each iteration x as a dictionary
# assigned to 1
def create_cycle():
    x = { }
    x[i+1] = x
    print(x)
 
# lists are cleared whenever a full collection or 
# collection of the highest generation (2) is run
collected = gc.collect() # or gc.collect(2)
print("Garbage collector: collected %d objects." % (collected))
 
print("Creating cycles...")
for i in range(10):
    create_cycle()
 
collected = gc.collect()
 
print("Garbage collector: collected %d objects." % (collected))


 
# Create some objects
obj1 = [1, 2, 3]
obj2 = {"a": 1, "b": 2}
obj3 = "Hello, world!"
 
gc.disable()

# c = gc.collect()
# print(c)
# Delete references to objects
del obj1
del obj2
del obj3
 
# Force a garbage collection
# c = gc.collect()
# print(c)
