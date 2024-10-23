import csv
import traceback

class Corporate:
    """
    A class to represent a Corporate customer.

    Attributes:
    -----------
    customer_id : str
        Unique identifier for the corporate customer (e.g., organizational number or VAT number).
    company_name : str
        The official name of the company.
    company_address : str
        The address of the company, formatted as a string or dictionary.
    reference_person : str
        The name of the reference person at the company.
    reference_contact : str
        Contact information of the reference person.
    invoice_email : str
        Email address for sending invoices.
    related_users : list
        List of related user IDs.
    customer_db : str
        Path to the CSV file for storing corporate customer data.
    """

    def __init__(self, customer_id, company_name, company_address, reference_person, reference_contact, 
                 invoice_email, related_users=None, customer_db="corporate.csv") -> None:
        """
        Initialize a Corporate object with the provided details.
        
        """
        self.customer_id = customer_id
        self.company_name = company_name
        self.company_address = company_address
        self.reference_person = reference_person
        self.reference_contact = reference_contact
        self.invoice_email = invoice_email
        self.related_users = related_users if related_users else []
        self.customer_db = customer_db

    @staticmethod
    def init_db(path: str):
        """
        Initialize the CSV file with headers.

        """
        with open(path, "w", newline="") as output_db:
            csv_writer = csv.writer(output_db)
            csv_writer.writerow([
                "customer_id", "company_name", "company_address", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])

    @staticmethod
    def save_to_csv(corporates, path: str):
        """
        Save multiple Corporate objects to the CSV file.

        """
        with open(path, "a", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "customer_id", "company_name", "company_address", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])
            for corporate in corporates:
                csv_writer.writerow(corporate.__dict__)

    @staticmethod
    def read_csv_file(path: str):
        """
        Read and print the contents of the CSV file.

        """
        try:
            print("Opening the file...")
            with open(path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=",")
                header = next(csv_reader, None)  # Read header
                print(f"Header: {header}")
                print("Reading rows...")
                for row in csv_reader:
                    print(f"Row: {row}")
                print("Done reading rows.")
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")

    @staticmethod
    def remove_from_csv(path: str, customer_id: str):
        """
        Remove a specific Corporate entry from the CSV file based on customer_id.

        """
        try:
            with open(path, "r") as file:
                csv_reader = csv.DictReader(file)
                rows = list(csv_reader)
                new_rows = [row for row in rows if row["customer_id"] != customer_id]

            if len(new_rows) < len(rows):
                with open(path, "w", newline="") as f:
                    csv_writer = csv.DictWriter(f, fieldnames=csv_reader.fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(new_rows)
                    print(f"Corporate entry with customer_id {customer_id} has been removed.")
            else:
                print(f"No corporate entry was found with customer_id {customer_id}")
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_csv(path: str, customer_id: str, updated_data: dict):
        """
        Update a specific Corporate entry in the CSV file based on customer_id.

        """
        try:
            with open(path, "r", newline="") as f:
                rows = list(csv.DictReader(f))

            updated = False
            for row in rows:
                if row["customer_id"] == customer_id:
                    row.update(updated_data)
                    updated = True
                    break
            
            if updated:
                with open(path, "w", newline="") as f:
                    csv_writer = csv.DictWriter(f, fieldnames=rows[0].keys())
                    csv_writer.writeheader()
                    csv_writer.writerows(rows)
                    print(f"Corporate entry with customer_id {customer_id} was updated.")
            else:
                print(f"No corporate entry was found with customer_id {customer_id}")

        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
            traceback.print_exc()

# Create a list of Corporate objects
corporates = [
    Corporate(
        customer_id="C001",  
        company_name="Global Corp.", 
        company_address="789 Maple St, Jane Smith",
        reference_person="John Doe", 
        reference_contact="312-456-7890", 
        invoice_email="billing@globalcorp.com",
        related_users=["jane@example.com"]
    ),
    Corporate(
        customer_id="C002",  
        company_name="Tech Solutions Ltd.", 
        company_address="456 Pine St, San Francisco, CA 94111",
        reference_person="John Doe", 
        reference_contact="415-789-4567", 
        invoice_email="billing@techsolutions.com",
        related_users=["john@example.com"]
    )
]

# Initialize the CSV file
Corporate.init_db("corporate.csv")

# Save the corporate objects to the CSV file
Corporate.save_to_csv(corporates, path="corporate.csv")

# Read the CSV file to verify the content
Corporate.read_csv_file("corporate.csv")

# Remove a corporate entry by customer_id
Corporate.remove_from_csv("corporate.csv", customer_id="C001")

# Update the corporate entry with customer_id "C002"
updated_data = {
    "company_name": "Tourism Innovations Ltd.",
    "invoice_email": "billing@techinnovations.com"
}
Corporate.update_csv("corporate.csv", customer_id="C002", updated_data=updated_data)
