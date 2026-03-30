from pydantic import BaseModel, ValidationError, Field
from datetime import datetime, UTC
from functools import partial
from typing import Literal,Annotated

class User(BaseModel):
    uid : Annotated[int, Field(gt=0)]
    username : Annotated[str, Field(min_length=3, max_length=20)]
    email : str
    age : Annotated[int, Field(ge=13,le=130)]

    verified_at : datetime | None = None

    bio : str = ""
    is_active : bool = True

    full_name : str | None = None

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


try:
    user = User(
        uid = 0,
        username="cs",
        email="ashwini@gmail.com",
        age=12

    )
except ValidationError as e:
    print(e)
# post = BlogPost(
#     title="Getting started with Python",
#     content="python is dynamically typing language.",
#     author_id="123",
# )

# print(post)