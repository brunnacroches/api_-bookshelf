from cerberus import Validator

def validate_create_book_request_body(request_body):
    # Define o esquema de validação
    schema = {
        "name": {"type": "string", "required": True},
        "year": {"type": "integer", "min": 0, "max": 3000, "required": True},
        "genre": {"type": "string", "allowed": ["Romance", "Biografia", "Técnico"], "required": True}
    }

    # Valida o body da requisição
    validator = Validator(schema)
    return validator.validate(request_body), validator.errors
