import platform
print(platform.python_implementation())

import sys
a = "my string"
print(sys.getrefcount(a))
b = [a]
c = {'key':a}

print(sys.getrefcount(a))