from models.book_model import DataBase, BookModel

# para cadastrar um novo livro
class BookController:
    def __init__(self):
        self.db_repository = DataBase()

    def create_book(self, name:str, year:int, genre:str):
        book = BookModel(name=name, year=year, genre=genre)
        self.db_repository.register_book(book)
        return book
