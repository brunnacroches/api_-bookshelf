from controller.get_books_controller import GetBooksByGenreController
from cerberus import Validator
from validators.validate_search_book import validate_search_book_request_body

class SearchBookView:
    def view_books(self, request):
        # Valida o body da requisição
        validation_response = validate_search_book_request_body(request.json)
        if not validation_response["is_valid"]:
            return {"status_code": 400, "data": {"error": validation_response["error"]}}
            
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