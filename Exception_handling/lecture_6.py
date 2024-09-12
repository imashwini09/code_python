# TO handle custom exception we need to create a class of it
# To make to a Exception we need o inherit from base Exception class

class TranscationFailed(Exception):
    def __init__(self,message):
        self.message = message

try:
    print("try something")
    raise TranscationFailed("failed transcation")
except RuntimeError:
    print("Runtime Error")
else:
    print("some other exception")