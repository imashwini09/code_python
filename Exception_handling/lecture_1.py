try:
    raise RuntimeError
    print("try something")
except RuntimeError:
    print("handling runtime exception")
finally:
    print("finally")