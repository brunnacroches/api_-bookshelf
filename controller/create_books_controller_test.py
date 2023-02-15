import unittest
from models.book_model import BookModel, DataBase
from controller.create_book_controller import BookController

class TestBookController(unittest.TestCase):
    def setUp(self):
        self.controller = BookController()

    def test_create_book_success(self):
        # Teste de sucesso
        book = self.controller.create_book("The Great Gatsby", 1925, "Fiction")
        self.assertIsInstance(book, BookModel)

def test_create_book_error(self):
    # Teste de erro - nome do livro inválido
    with self.assertRaises(ValueError):
        self.controller.create_book("", 1925, "Fiction")

    # Teste de erro - ano do livro inválido
    with self.assertRaises(TypeError):
        self.controller.create_book("The Catcher in the Rye", "1951", "Fiction")

    # Teste de erro - gênero do livro inválido
    with self.assertRaises(ValueError):
        self.controller.create_book("Pride and Prejudice", 1813, "")
