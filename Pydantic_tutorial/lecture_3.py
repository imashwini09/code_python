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

try:
    user = User(
        uid = 1,
        username=None,
        email = 123,
    )

    # print(user)
except ValidationError as e:
    print(e)


# user.bio = "Python dev"
# error because user object not created because of 2 validation error in try block
# print(user.model_dump_json(indent=2))