from flask import jsonify
from ..models import Customer, db
from app.models import Customer  # Import your Customer model

class CustomerController:
    @staticmethod
    def get_all_customers():
        # Example implementation to get all customers
        customers = Customer.query.all()
        return jsonify([customer.serialize() for customer in customers])

    # Implement other CRUD operations for customers (get_customer, add_customer, update_customer, delete_customer, etc.)

    @staticmethod
    def get_customer(customer_id):
        customer = Customer.query.get(customer_id)
        if customer:
            return jsonify(customer.to_dict()), 200
        return jsonify({"error": "Customer not found"}), 404

    @staticmethod
    def add_customer(data):
        new_customer = Customer(
            name=data.get('name'),
            phone_number=data.get('phone_number'),
            email=data.get('email'),
            address=data.get('address')
        )
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(new_customer.to_dict()), 201

    @staticmethod
    def update_customer(customer_id, data):
        customer = Customer.query.get(customer_id)
        if customer:
            customer.name = data.get('name', customer.name)
            customer.phone_number = data.get('phone_number', customer.phone_number)
            customer
