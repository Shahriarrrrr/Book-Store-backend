from fastapi import FastAPI
from pydantic import BaseModel, Field
import typing
app = FastAPI()


class Book:
    id:int
    title:str
    author:str
    description:str
    rating:int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: typing.Optional[int] = None
    title: str = Field(min_length=3, max_length=20)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating:int = Field(gt=0 , lt=6)


BOOKS =  [
    Book(1, "Computer Science Pro",  'codingwithrobu', 'A very nice book!', 2),
    Book(2, "Pir E Kamil",  'Umera Hayat', 'Great Book!', 5),
    Book(3, "Abe Hayat",  'Umera Hayat', 'Greatest', 5),
    Book(4, "Electrical with electrics",  'capacitorbros', 'Electrifying book!', 1),
    Book(5, "Harry Potter",  'J.K Rowling', 'Mystery book!', 4),
    Book(6, "Adventures of Rumi",  'Rumi', 'Folk stories!', 3),
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request : BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id_and_increment(new_book))


def find_book_id_and_increment(book : Book):
    book.id = 1 if(len(BOOKS) == 0) else BOOKS[-1].id + 1
    return book        