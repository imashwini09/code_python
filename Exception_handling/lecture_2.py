# even after 8th line throwing error finally block will execute

try:
    raise RuntimeError
    print("try something")
except RuntimeError:
    print("handling runtime exception")
    raise RuntimeError
    print("handling error again")
finally:
    print("finally")