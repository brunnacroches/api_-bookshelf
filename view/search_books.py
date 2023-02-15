from controller.get_books_controller import GetBooksByGenreController

class SearchBookView:
    def view_books(self, request):
        body = request.json
        genre = body["genre"]

        search_book_controler = GetBooksByGenreController
        search_book_controler.get_books_by_genre(genre)

        return {
            "status_code": 200,
            "data": {
                "genre": genre
            },
            "success": True
        }