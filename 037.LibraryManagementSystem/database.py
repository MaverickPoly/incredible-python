import sqlite3
from typing import Sequence, List

FILENAME = "movies.db"


class Book:
    def __init__(self, id: int, title: str, author: str, rating: float):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

    @staticmethod
    def from_sequence(sequence: Sequence) -> Book:
        return Book(sequence[0], sequence[1], sequence[2], sequence[3])


class BooksDatabase:
    def __init__(self):
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                rating FLOAT NOT NULL DEFAULT 0
            )
            """)

    @staticmethod
    def add_book(title: str, author: str, rating: float) -> None:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books (title, author, rating) 
                VALUES (?, ?, ?)
            """, (title, author, rating))

    @staticmethod
    def get_books() -> List[Book]:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM books
            """)
            return list(map(Book.from_sequence, cursor.fetchall()))

    @staticmethod
    def delete_book(id: int) -> int:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM books WHERE id=?
            """, (id,))
            return cursor.rowcount

    @staticmethod
    def update_book(id: int, title: str, author: str, rating: float) -> int:
        with sqlite3.connect(FILENAME) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE books SET title=?, author=?, rating=?
                WHERE id=?
            """, (title, author, rating, id))
            return cursor.rowcount
