# To stop Finally block abruptly

try:
    raise RuntimeError
    print("try something")
finally:
    raise RuntimeError
    print("finally")