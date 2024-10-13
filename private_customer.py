class PrivateCustormer:
    def __init__(self, customer_id, reference_person, reference_contact, 
                 invoice_email, related_users=None, customer_db="customers.csv") -> None:
        self.customer_id = customer_id  # Unique identifier (e.g., organizational number or VAT number)
        self.reference_person = reference_person  # Full name of reference person
        self.reference_contact = reference_contact  # Contact info as a dict {'mobile': '', 'email': ''}
        self.invoice_email = invoice_email  # Email address for invoices
        self.related_users = related_users if related_users else []  # List of user IDs
        self.customer_db = customer_db  # Path to CSV file for storing customer data