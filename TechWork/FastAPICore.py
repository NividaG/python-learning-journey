from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    price: float = Field(gt=0)


@app.get("/")
def home():
    return {"message": "FastAPI is running"}


@app.get("/books/{book_id}")
def get_book(book_id: int):
    return {
        "book_id": book_id,
        "title": "Sample Book"
    }


@app.post("/books")
def create_book(book: Book):
    return {
        "message": "Book created successfully",
        "book": book
    }

@app.get("/search")
def search_books(q: str, limit: int = 10):
    return {"query": q, "limit": limit}