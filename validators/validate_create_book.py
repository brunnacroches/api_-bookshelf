from cerberus import Validator

# Define o esquema de validação
validator_create = Validator({
    "data": {
        "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True},
                "year": {"type": "integer", "min": 0, "max": 3000, "required": True},
                "genre": {"type": "string", "allowed": ["Romance", "Biografia", "Técnico"], "required": True}
        }
    },
})

request_body = {
        "data": {
            "name": "The Alchemist",
            "year": 1988,
            "genre": "Romance"
        }
    }

def validate_create_book_request_body(request_body):
    response = validator_create.validate(request_body)

    if response is False:
        print(validator_create.errors)
    else:
        print('Request body OK!')
