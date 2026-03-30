from pydantic import BaseModel, EmailStr,field_validator

class User(BaseModel):
    name : str
    email : EmailStr
    account_id : int

    @field_validator("account_id")
    def validate_account_id(cls,value):
        if value <= 0:
            raise ValueError
        return value

user = User(name ="Ashwini", email = "ashwini@gmail.com", account_id=10)
print(user.name)