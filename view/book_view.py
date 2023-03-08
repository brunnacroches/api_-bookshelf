from cerberus import Validator
from controller.create_book_controller import BookController
from validators.validate_create_book import validate_create_book_request_body

class BookView:
    def view_books(self, request):
        # Valida o body da requisição
        validation_response = validate_create_book_request_body(request.json)
        if not validation_response["is_valid"]:
            return {"status_code":400, "data": { "error" : validation_response["error"]}}

        # Extrai os valores do livro do body da requisição
        body = request.json
        name = body["name"]
        year = body["year"]
        genre = body["genre"]

        # Chama o controlador para criar o livro
        create_book_controler = BookController()
        create_book_controler.create_book(name, year, genre)

        # Retorna os resultados
        return {
            "status_code": 200,
            "data": {
                "name": name,
                "year": year,
                "genre": genre
            },
            "success": True
        }
