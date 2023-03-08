from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import validates
from sqlalchemy import ForeignKey

Base = declarative_base()

class GenreModel(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)

    valid_names = ["Romance", "Biografia", "Técnico"]

    @validates('name')
    def validate_name(self, key, name):
        if not any(substring in name for substring in self.valid_substrings):
            raise ValueError(f"Invalid genre '{name}'. Must contain one of {self.valid_substrings}.")
        return name

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)
    genre = relationship(GenreModel, backref="books")


class DataBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///my_database.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def register_book(self, name:str, year: int, genre: str):
        session = self.Session()
        genre_model = session.query(GenreModel).filter_by(name=genre).first()
        if not genre_model:
            raise ValueError(f"Invalid genre '{genre}'. Must be one of {GenreModel.valid_names}.")
        book_model = BookModel(name=name, year=year, genre=genre_model)
        session.add(book_model)
        session.commit()
        session.close()

    def search_book_genre(self, genre:str):
        session = self.Session()
        genre_model = session.query(GenreModel).filter_by(name=genre).first()
        if not genre_model:
            return []
        books = session.query(BookModel).filter_by(genre=genre_model).all()
        session.close()
        return books


class BookController:
    def __init__(self):
        self.db_repository = DataBase()

    def create_book(self, name:str, year:int, genre:str):
        self.db_repository.register_book(name, year, genre)

    def get_books_by_genre(self, genre:str):
        return self.db_repository.search_book_genre(genre)
