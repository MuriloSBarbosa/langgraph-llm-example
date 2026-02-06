from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass
class Book:
    """
    Represents a book with its metadata.

    Args:
        id (int): Identification of the book
        title (str): Title of the book. Cannot be null or empty.
        genre (str): Literary genre or category. Cannot be null or empty.
        author (str): Author of the book. Cannot be null or empty.
        release_date (datetime): Publication or release date.
        rating (Decimal): Rating score (0.0 to 9.9).
        description (str): Short textual description of the book.
    """

    id: str
    title: str
    genre: str
    director: str
    release_date: datetime
    rating: Decimal
    description: str
