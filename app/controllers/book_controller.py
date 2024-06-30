from flask import jsonify
from app.models import Book
from app.extensions import db
from datetime import datetime





class BookController:
    @staticmethod
    def get_all_books():
        # Example implementation to get all books
        books = Book.query.all()
        return jsonify([book.serialize() for book in books])

    @staticmethod
    def get_book(book_id):
        # Example implementation to get a specific book by ID
        book = Book.query.get_or_404(book_id)
        return jsonify(book.serialize())

    # Implement other CRUD operations for books (add_book, update_book, delete_book, etc.)

    @staticmethod
    def add_book(data):
        title = data.get('title')
        author = data.get('author')
        published_date_str = data.get('published_date')

        # Convert the published_date string to a date object
        published_date = datetime.strptime(published_date_str, '%Y-%m-%d').date()

        new_book = Book(title=title, author=author, published_date=published_date)
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book added successfully"}, 201

    @staticmethod
    def update_book(book_id, data):
        book = Book.query.get(book_id)
        if book:
            book.title = data['title']
            book.author = data['author']
            book.published_date = data['published_date']
            db.session.commit()
            return jsonify(book.to_dict())
        return jsonify({'message': 'Book not found'}), 404

    @staticmethod
    def delete_book(book_id):
        book = Book.query.get(book_id)
        if book:
            db.session.delete(book)
            db.session.commit()
            return jsonify({'message': 'Book deleted'})
        return jsonify({'message': 'Book not found'}), 404
