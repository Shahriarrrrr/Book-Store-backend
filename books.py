from fastapi import FastAPI, Body

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
async def create_book(book_request = Body()):
    BOOKS.append(book_request)