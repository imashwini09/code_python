from pydantic import BaseModel, ValidationError, Field, EmailStr, HttpUrl, SecretStr, computed_field, field_validator, model_validator
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
    first_name : str | None = None
    last_name : str | None = None
    followers_count : int = 0

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
    
    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.followers_count >= 10000

class Comment(BaseModel):
    content : str
    author_email : EmailStr
    likes : int = 0

class BlogPost(BaseModel):
    title : Annotated[str, Field(min_length=1,max_length=200)]
    content : Annotated[str, Field(min_length=20)]
    author : User
    view_count : int = 0
    is_published : bool = False

    tags : list[str] = Field(default_factory=list)

    # create_at : datetime = Field(default_factory=lambda : datetime.now(tz=UTC))
    # both will do same work lambda or partial function
    create_at : datetime = Field(default_factory=partial(datetime.now,tz=UTC))

    author_id : str | int | None = None
    status : Literal["draft", "published", "archived"] = "draft"

    slug : Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

    comments : list[Comment] = Field(default_factory=list)


class UserRegistration(BaseModel):
    email : EmailStr
    password : str
    confirm_password : str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

user = User(
    username="Ashwini_123",
    email="ashwini@gmail.com",
    age=25,
    password="mysecretpassword",
    website="www.ashwini.com",
    # first_name="Ashwini",
    # last_name="Samal",
    # followers_count=15000,
)

# print(user.display_name)  # Output: Ashwini Samal
# print(user.is_influencer)  # Output: True
# print(user.model_dump_json(indent=2))

post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "slug": "understanding-pydantic",
    "author": user,
    "author_id": "coreyms-1",
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data)

print(post.model_dump_json(indent=2))
