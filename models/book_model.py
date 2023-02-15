from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


# Define a classe Book que herda de db.Model
class BookModel(Base):
    # Nome da tabela no banco de dados
    __tablename__ = "books"

    # Define as colunas da tabela
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    genre = Column(String(20), nullable=False)

class DataBase:
    def __init__(self):
        self.engine = create_engine('sqlite:///my_database.db') #!! # Não existe o banco pessoas.db no projeto
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def register_book(self, book):
        session = self.Session()
        book_model = BookModel(name=book.name, year=book.year, genre=book.genre)
        session.add(book_model)
        session.commit()
        session.close()
    
    def search_book_genre(self, genre:str):
        session = self.Session()
        book_model = session.query(BookModel).filter_by(genre=genre).first()
        session.close()
        return book_model
