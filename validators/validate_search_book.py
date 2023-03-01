from cerberus import Validator

def validate_search_book_request_body(request_body):
    search_book_schema = {
        "genre": {"type": "string", "required": True, "empty": False},
    }
    # Valida o body da requisição
    validator = Validator(search_book_schema)
    return validator.validate(request_body), validator.errors
