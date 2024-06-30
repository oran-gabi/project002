# backend/app/controllers/loan_controller.py
from app.models import Loan , db 
from flask import jsonify

class LoanController:
    @staticmethod
    def get_all_loans():
        # Example implementation to get all loans
        loans = Loan.query.all()
        return jsonify([loan.serialize() for loan in loans])

    # Implement other CRUD operations for loans (get_loan, add_loan, update_loan, delete_loan, etc.)

    @staticmethod
    def get_loan(loan_id):
        return Loan.query.get(loan_id).serialize()

    @staticmethod
    def create_loan(data):
        new_loan = Loan(**data)
        db.session.add(new_loan)
        db.session.commit()
        return new_loan.serialize()

    @staticmethod
    def update_loan(loan_id, data):
        loan = Loan.query.get(loan_id)
        if not loan:
            return None
        for key, value in data.items():
            setattr(loan, key, value)
        db.session.commit()
        return loan.serialize()

    @staticmethod
    def delete_loan(loan_id):
        loan = Loan.query.get(loan_id)
        if not loan:
            return False
        db.session.delete(loan)
        db.session.commit()
        return True
