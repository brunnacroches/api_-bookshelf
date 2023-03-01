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
        self.engine = create_engine('sqlite:///my_database.db') #!! # Não existe o banco pessoas.db no projeto
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def register_book(self, book):
        session = self.Session()
        genre_model = session.query(GenreModel).filter_by(name=book.genre).first()
        if not genre_model:
            raise ValueError("Invalid genre")
        book_model = BookModel(name=book.name, year=book.year, genre_id=genre_model.id)
        session.add(book_model)
        session.commit()
        session.close()

    def search_book_genre(self, genre:str):
        session = self.Session()
        genre_model = session.query(GenreModel).filter_by(name=genre).first()
        if not genre_model:
            return []
        books = session.query(BookModel).filter_by(genre_id=genre_model.id).all()
        session.close()
        return books

