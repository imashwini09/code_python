from pydantic import BaseModel

class User(BaseModel):
    username : str
    email : str
    age : int

user1 = User(username="Ashwini", email= "ashwini@gmail.com", age= 26)
print(user1)

# user2 = User(username="badal", email=None, age=25)
# print(user2)
# Error for email

