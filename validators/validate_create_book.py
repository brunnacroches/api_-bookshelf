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
    is_valid = validator.validate(request_body)
    
    # return validator.validate(request_body), validator.errors
    # aqui colocar o validator.validate junto com o validatr.erros, não é uma boa prática,
    # então separamos esses dados dentro de um dicionário
    validation_response = {
        "is_valid": is_valid,
        "error": validator.errors
    }

    return validation_response

