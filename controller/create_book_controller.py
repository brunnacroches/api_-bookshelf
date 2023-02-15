from models.book_model import DataBase, BookModel

# para cadastrar um novo livro
class BookController:
    def __init__(self):
        self.bd_repositorio = DataBase()

    def create_book(self, name:str, year:int, genre:str):
        book = BookModel(name=name, year=year, genre=genre)
        return book
