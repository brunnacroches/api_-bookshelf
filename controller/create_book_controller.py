from models.book_model import DataBase, BookModel

# para cadastrar um novo livro
class BookController:
    def __init__(self):
        self.db_repository = DataBase()

    def create_book(self, name:str, year:int, genre:str):
        # book = BookModel(name=name, year=year, genre=genre)
        # self.db_repository.register_book(book)
        # return book
        # ! no caso o código estava redundante porque o banco de dados 
        # ! já está fazendo a sua criação, então aqui usamos o controller
        # ! apenas para coletar essas informações vindas da view(body) pelo 
        # ! usuário e joga para models o banco de dados
        self.db_repository.register_book(name, year, genre)
