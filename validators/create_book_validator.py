from cerberus import Validator

# def validar_body():
    # esquema de validação
    # se der erro, voltar informação para usuario
    # se nao der erro, continuar o processo normalmente
def validate_search_book_request_body(request_body):
    search_book_schema = Validator ({
        "data": {
            "type": "dict",
            "schema": {
                "genre": {"type": "string", "required": True, "empty": False},
            }
        },
    })
     # Valida o body da requisição
    validator = Validator(search_book_schema)
    return validator.validate(request_body), validator.errors

def validate_create_book_request_body(request_body):
    create_book_schema = Validator ({
        "data": {
            "type": "dict",
            "schema": {
                "name": {"type": "string", "required": True, "empty": False},
                "year": {"type": "inter", "required": True, "empty": False},
                "genre": {"type": "string", "required": True, "empty": False, 'allowed': ['Romance', 'Biografia', 'Tecnico']},
            }
        },
    })
    # Valida o body da requisição
    validator = Validator(create_book_schema)
    return validator.validate(request_body), validator.errors


# response = validation_body.validade(body)

# if response is False:
#     print(validation_body.erros)
# else:
#     print('Body OK!')