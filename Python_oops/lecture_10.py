# while True:
#     try:    
#         x = int(input("value of x "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x value is {x}")


def bool_return():
    try:
        print("hi")
        return True
    finally:
        print("hello")
        return False

print(bool_return())