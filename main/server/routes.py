from flask import request, jsonify
from .server import app
from view.book_view import BookView
from view.search_books import GetBooksByGenreController

@app.route("/books", methods=["POST"])
def create_book():
    book_view = BookView()
    
    http_response = book_view.view_books(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/books/search", methods=["POST"])
def search_books():
    action_search_product = GetBooksByGenreController()

    http_response = action_search_product.get_books_by_genre(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]
