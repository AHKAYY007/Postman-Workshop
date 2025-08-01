from pydantic import BaseModel

class BookBase(BaseModel):
    id: int
    title: str
    content: str
    author: str
    published: bool

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class BookResponse(BaseModel):
    id: int
    title: str
    content: str
    class config:
        from_attributes = True