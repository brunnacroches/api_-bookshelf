from controller.create_book_controller import BookController

class BookView:
    def view_books(self, request):
        body = request.json
        name = body["name"]
        year = body["year"]
        genre = body["genre"]

        create_book_controler = BookController()
        create_book_controler.create_book(name, year, genre)

        return {
            "status_code": 200,
            "data": {
                "name": name,
                "year": year,
                "genre": genre
            },
            "success": True
        }