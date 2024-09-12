#  try except and else

try:
    print("try something")
except RuntimeError:
    print("handling runtime exception")
else:
    print("No exception found")

try:
    print("try something")
    raise RuntimeError
except RuntimeError:
    print("handling runtime exception")
else:
    print("No exception found")