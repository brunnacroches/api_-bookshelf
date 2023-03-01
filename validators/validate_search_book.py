from cerberus import Validator

def validate_search_book_request_body(request_body):
    search_book_schema = {
        "genre": {"type": "string", "required": True, "empty": False},
    }
    # Valida o body da requisição
    validator = Validator(search_book_schema)
    is_valid = validator.validate(request_body)
    
    validation_response = {
        "is_valid": is_valid,
        "error": validator.errors
    }
    
    return validation_response
    # return validator.validate(request_body), validator.errors
