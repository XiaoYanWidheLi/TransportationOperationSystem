class PaymentDetails:

    def __init__(self, payment_method, transaction_id, amount, payment_status, card_information=None, payment_db="payment_details.csv"):
        """
        Initialize a PaymentDetails object.
        - payment_method: The method of payment (e.g., 'Net Banking', 'Credit Card', 'Debit Card').
        - transaction_id: A unique identifier for the transaction.
        - amount: The payment amount (in € or SEK).
        - payment_status: The status of the payment ('Paid' or 'Unpaid').
        - card_information: Optional; a dictionary containing card details if the payment is made by card.
          Format: {'card_number': '1234567812345678', 'cardholder_name': 'John Doe'}
        - payment_db: Path to the CSV file to store payment details.
        """
        self.payment_method = payment_method
        self.transaction_id = transaction_id
        self.amount = amount
        self.payment_status = payment_status
        self.card_information = card_information
        self.payment_db = payment_db

    def payment_method(self, method):
        """
        Set or update the payment method.
        - method: The method of payment to be set (must be one of the allowed methods).
        """
        allowed_methods = ["Net Banking", "Credit Card", "Debit Card"]  # Define allowed methods inside the method
        if method in allowed_methods:
            self.payment_method = method
            print(f"Payment method set to '{method}'.")
        else:
            raise ValueError(f"Invalid payment method '{method}'. Choose from {allowed_methods}.")

    def payment_status(self, new_status):
        """
        Update the payment status.
        - new_status: The new payment status ('Paid' or 'Unpaid').
        """
        if new_status in ["Paid", "Unpaid"]:
            self.payment_status = new_status
            print(f"Payment status updated to {new_status}.")
        else:
            print("Invalid status. Please choose 'Paid' or 'Unpaid'.")

    def card_info(self):
        """
        Display masked card information (only show last 4 digits) if card payment is used.
        """
        if self.card_information:
            card_number = self.card_information.get('card_number', '')
            cardholder_name = self.card_information.get('cardholder_name', '')
            masked_card = f"**** **** **** {card_number[-4:]}"
            return f"Cardholder: {cardholder_name}, Card Number: {masked_card}"
        else:
            return "No card information available."