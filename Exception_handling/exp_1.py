def bool_return():
    try:
        return 1
    finally:
        return 0

print(bool_return())