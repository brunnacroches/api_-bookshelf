from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import ForeignKey

Base = declarative_base()

# Define a tabela de gêneros
class GenreModel(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

# Define a tabela de livros
class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)
    genre = relationship(GenreModel)


class DataBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///my_database.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

# ! mudamos os parametros de 'book' para 'name','year' e 'genre' por conta da 
# ! alteração no controller, corrigimos a redundancia então a criação e armazenamento
# ! destes dados será aqui
    def register_book(self, name:str, year: int, genre: str):
        session = self.Session()
        # genre_model = session.query(GenreModel).filter_by(name=book.genre).first()
        # ! desse modo não precisa mais chamar o 'book' no genre
        genre_model = session.query(GenreModel).filter_by(name=genre).first()
        if not genre_model:
            raise ValueError("Invalid genre")
        # ! e também não precisa chamar mais o book no name e year
        # book_model = BookModel(name=book.name, year=book.year, genre_id=genre_model.id)
        book_model = BookModel(name=name, year=year, genre_id=genre_model.id)
        session.add(book_model)
        session.commit()
        session.close()

    def search_book_genre(self, genre:str):
        # Aqui inicializamos a sessão
        session = self.Session()
        # Criamos o filtro de busca pelo nome do género
        genre_model = session.query(GenreModel).filter_by(name=genre).first()

        # se o nome não estiver dentro da lista de géneros disponíveis
        if not genre_model:
            # retornará uma lista vazia
            return []
        # se tiver inicia uma outra sessão filtrando e apresentando todos os nomes
        # de livros que tem naquele genero buscado
        books = session.query(BookModel).filter_by(genre_id=genre_model.id).all()
        # depois disso encerra a sessão
        session.close()
        # e retorna os livros
        return books

