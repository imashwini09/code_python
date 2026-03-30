# Example of string interning
a = "hello"
b = "hello"
print(a is b)  # True (interned, same memory address)
print(id(a))
print(id(b))

c = "hello world" * 100  # Runtime-generated string
d = "hello world" * 100
print(c is d)  # False (not interned, different objects)

# Explicit interning
import sys
c_interned = sys.intern(c)
d_interned = sys.intern(d)
print(c_interned is d_interned)  # True (interned explicitly)
