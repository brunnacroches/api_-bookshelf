from controller.get_books_controller import GetBooksByGenreController
from cerberus import Validator
from validators import validate_search_book_request_body

class SearchBookView:
    def view_books(self, request):
        # Valida o body da requisição
        validator = Validator(validate_search_book_request_body())
        is_valid = validator.validate(request.json)
        errors = validator.errors
        if not is_valid:
            return {"status_code": 400, "error": errors, "success": False}

        # Extrai os valores do livro do body da requisição
        body = request.json
        genre = body["genre"]

        # Chama o controlador para criar o livro
        search_book_controler = GetBooksByGenreController
        book = search_book_controler.get_books_by_genre(genre)

        # Retorna os resultados
        return {
            "status_code": 200,
            "data": {
                "genre": book
            },
            "success": True
        }