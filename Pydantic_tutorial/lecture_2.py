from pydantic import BaseModel, ValidationError
from datetime import datetime

class User(BaseModel):
    uid : int
    username : str
    email : str

    verified_at : datetime | None = None

    bio : str = ""
    is_active : bool = True

    full_name : str | None = None

user = User(
    uid = 1,
    username="Ashwini",
    email = "ashwini@gmail.com"
)

# print(user)

print(user.username)

# user.bio = 123
# This will work even if 123 is not a string
# print(user.bio)

user.bio = "Python dev"

print(user.model_dump_json(indent=2))