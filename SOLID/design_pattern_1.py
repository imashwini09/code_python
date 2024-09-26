# Singleton Dp

# Create a class with only 1 instance possible
# It follows monogamy

# Example : once the Db connection is build use that same pipeline, Do not create the new connection

class singleton:
    __instance = None

    def __new__(cls, *args, **kwagrs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

if __name__ == "__main__":
    instance = singleton()
    print(instance)
    instance2 = singleton()
    print(instance2)
    print(instance is instance2)