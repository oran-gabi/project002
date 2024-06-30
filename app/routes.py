from flask import Blueprint, jsonify, request, render_template
from app.controllers.book_controller import BookController
from app.controllers.customer_controller import CustomerController
from app.controllers.loan_controller import LoanController

api = Blueprint('api', __name__)

# Authentication page
@api.route('/auth', methods=['GET'])
def auth_page():
    return render_template('auth.html')

# Register endpoint
@api.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Placeholder for actual registration logic
    # Example: Save username and password to database
    # Replace this with your actual database logic
    if username and password:
        # Example response, replace with actual logic
        return jsonify({"success": True, "message": "Registration successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid data. Please try again."})

# Login endpoint
@api.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Placeholder for actual login logic
    # Example: Check username and password against database
    # Replace this with your actual database logic
    if username == 'testuser' and password == 'password':
        return jsonify({"success": True, "message": "Login successful!"})
    else:
        return jsonify({"success": False, "message": "Invalid username or password."})
# Book routes
@api.route('/books', methods=['GET'])
def get_books():
    return BookController.get_all_books()

@api.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return BookController.get_book(book_id)


# add on thunder name: add car:http://127.0.0.1:5000/api/books

@api.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    print(data)
    return BookController.add_book(data)

@api.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    return BookController.update_book(book_id, data)

@api.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    return BookController.delete_book(book_id)

# Customer routes
@api.route('/customers', methods=['GET'])
def get_customers():
    return CustomerController.get_all_customers()

@api.route('/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    return CustomerController.get_customer(customer_id)

@api.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()
    return CustomerController.add_customer(data)

@api.route('/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    data = request.get_json()
    return CustomerController.update_customer(customer_id, data)

@api.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    return CustomerController.delete_customer(customer_id)

# Loan routes
@api.route('/loans', methods=['GET'])
def get_loans():
    return LoanController.get_all_loans()

@api.route('/loans/<int:loan_id>', methods=['GET'])
def get_loan(loan_id):
    return LoanController.get_loan(loan_id)

@api.route('/loans', methods=['POST'])
def add_loan():
    data = request.get_json()
    return LoanController.add_loan(data)

@api.route('/loans/<int:loan_id>', methods=['PUT'])
def update_loan(loan_id):
    data = request.get_json()
    return LoanController.update_loan(loan_id, data)

@api.route('/loans/<int:loan_id>', methods=['DELETE'])
def delete_loan(loan_id):
    return LoanController.delete_loan(loan_id)
