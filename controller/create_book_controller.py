from models.book_model import DataBase

# para cadastrar um novo livro
class BookController:
    def __init__(self):
        self.db_repository = DataBase()

    def create_book(self, name:str, year:int, genre:str):
        self.db_repository.register_book(name, year, genre)
