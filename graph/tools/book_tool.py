from langchain.tools import tool
import repository.book_repository as repository
from typing import List
from models import *


@tool
def find_all_books() -> List[dict]:
    """
    Find all books in DataBase

    Returns:
        List[Book]
    """
    books = repository.find_all_books()
    print(books)
    return [
        {
            "id": book.id,
            "title": book.title,
            "genre": book.genre,
            "director": book.director,
            "release_date": book.release_date.isoformat(),
            "rating": float(book.rating),
            "description": book.description,
        }
        for book in books
    ]


@tool
def find_by_id(id: int) -> Book:
    """
    Find a books in DataBase by id

    args:
        id (Int): Id to find in Database

    Returns:
        Book
    """
    return repository.find_by_id(id)


@tool
def insert_book(book: Book):
    """
    Insert a book record into the database.

    Args:
        book (Book): Book entity containing all required data to be persisted.

    Returns:
        None
    """
    return repository.insert_book(book)
