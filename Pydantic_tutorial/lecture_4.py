from pydantic import BaseModel, ValidationError, Field
from datetime import datetime, UTC
from functools import partial
from typing import Literal

class User(BaseModel):
    uid : int
    username : str
    email : str

    verified_at : datetime | None = None

    bio : str = ""
    is_active : bool = True

    full_name : str | None = None

class BlogPost(BaseModel):
    title : str
    content : str
    view_count : int = 0
    is_published : bool = False

    tags : list[str] = Field(default_factory=list)

    # create_at : datetime = Field(default_factory=lambda : datetime.now(tz=UTC))
    # both will do same work lambda or partial function
    create_at : datetime = Field(default_factory=partial(datetime.now,tz=UTC))

    author_id : str | int
    status : Literal["draft", "published", "archived"] = "draft"

post = BlogPost(
    title="Getting started with Python",
    content="python is dynamically typing language.",
    author_id="123",
)

print(post)