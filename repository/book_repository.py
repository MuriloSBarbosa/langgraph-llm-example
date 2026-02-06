import psycopg2
from models import *
from typing import List


def get_connection():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="postgres",
        user="postgres",
        password="password",
    )


def find_all_books() -> list[Book]:
    with get_connection().cursor() as cursor:
        cursor.execute(
            """
            SELECT id, title, genre, director, release_date, rating, description
            FROM langgraph.book
        """
        )
        rows = cursor.fetchall()

    return [
        Book(
            id=row[0],
            title=row[1],
            genre=row[2],
            director=row[3],
            release_date=row[4],
            rating=row[5],
            description=row[6],
        )
        for row in rows
    ]


def find_by_id(id: int) -> Book:
    with get_connection().cursor() as cursor:
        cursor.execute(
            "SELECT * FROM langgraph.book WHERE id = %s;",
            (id,),
        )
        return cursor.fetchone()


def insert_book(book: Book):
    query = """
        INSERT INTO langgraph.book (
            title,
            genre,
            director,
            release_date,
            rating,
            description
        )
        VALUES (%s, %s, %s, %s, %s, %s);
    """

    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                query,
                (
                    book.title,
                    book.genre,
                    book.director,
                    book.release_date,
                    book.rating,
                    book.description,
                ),
            )
        connection.commit()
