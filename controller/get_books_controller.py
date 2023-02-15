from controller.create_book_controller import BookController
from models.book_model import DataBase

# get_books_by_genre, para buscar todos os livros de um gênero específico
class GetBooksByGenreController(BookController):
    def __init__(self):
        self.db_repository = DataBase()

    def get_books_by_genre(self, genre):
        books = self.db_repository.search_book_genre(genre)
        return books
        # DataBase.query.filter_by(genre=genre).all()
    