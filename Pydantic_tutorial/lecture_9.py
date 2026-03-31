from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl, SecretStr, field_validator, model_validator
from datetime import datetime, UTC
from functools import partial
from uuid import UUID, uuid4
from typing import Literal,Annotated

class User(BaseModel):
    uid : UUID = Field(default_factory=uuid4)   
    username : Annotated[str, Field(min_length=3, max_length=20)]
    email : EmailStr
    age : Annotated[int, Field(ge=13,le=130)]

    website : HttpUrl | None = None
    password : SecretStr

    verified_at : datetime | None = None

    bio : str = ""
    is_active : bool = True

    full_name : str | None = None

    @field_validator("username")
    @classmethod
    def validate_username(cls, v : str) -> str:
        if not v.replace("_","").isalnum():
            raise ValueError("Username must be alphanumeric or contain underscores")
        return v.lower()
    
    @field_validator("website", mode="before")
    @classmethod
    def add_https(cls, v : str | None) -> str | None:
        if v and not v.startswith(("http://","https://")):
            return f"https://{v}"
        return v

class BlogPost(BaseModel):
    title : Annotated[str, Field(min_length=1,max_length=200)]
    content : Annotated[str, Field(min_length=20)]
    view_count : int = 0
    is_published : bool = False

    tags : list[str] = Field(default_factory=list)

    # create_at : datetime = Field(default_factory=lambda : datetime.now(tz=UTC))
    # both will do same work lambda or partial function
    create_at : datetime = Field(default_factory=partial(datetime.now,tz=UTC))

    author_id : str | int
    status : Literal["draft", "published", "archived"] = "draft"

    slug : Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]


class UserRegistration(BaseModel):
    email : EmailStr
    password : str
    confirm_password : str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

try:
    registration = UserRegistration(
        email="ashwini@gmail.com",
        password="mysecretpassword",
        confirm_password="mysecretpassword1",
    )
except ValidationError as e:
    print(e)
    