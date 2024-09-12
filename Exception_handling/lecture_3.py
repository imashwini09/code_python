
try:
    raise RuntimeError
    print("try something")
finally:
    print("finally")