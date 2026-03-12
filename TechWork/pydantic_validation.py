from pydantic import BaseModel, Field

class Book(BaseModel):
    title: str
    author: str
    price: float = Field(ge=0)

data = {
    "title": "Python",
    "author": "Alex",
    "price": 200
}

book = Book(**data)

print(book)
print(book.model_dump())