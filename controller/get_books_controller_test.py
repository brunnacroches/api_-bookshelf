import unittest
from unittest.mock import MagicMock
from models.book_model import DataBase, BookModel
from controller.get_books_controller import GetBooksByGenreController

class TestGetBooksByGenreController(unittest.TestCase):
    def setUp(self) -> None:
        self.controller = GetBooksByGenreController()
        self.mock_db_repository = MagicMock(spec=DataBase)
        self.controller.db_repository = self.mock_db_repository
    
    def test_get_books_by_genre_with_valid_genre(self):
        self.mock_db_repository.search_book_genre.return_value = [("Fantasia")]

        book = self.controller.get_books_by_genre("Fantasia")
    
        self.mock_db_repository.search_book_genre.assert_called_once_with("Fantasia")

        self.assertEqual(book,[("Fantasia")])

    def test_get_books_by_genre_with_invalid_genre(self):

        self.mock_db_repository.search_book_genre.return_value = []

        books = self.controller.get_books_by_genre("Invalid Genre")

        self.mock_db_repository.search_book_genre.assert_called_once_with("Invalid Genre")

        self.assertEqual(books, [])


