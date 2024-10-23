import csv
class PrivateCustormer:
    def __init__(self, customer_id, reference_person, reference_contact, 
                 invoice_email, related_users=None, customer_db="private_customers.csv") -> None:
        self.customer_id = customer_id  # Unique identifier (e.g., organizational number or VAT number)
        self.reference_person = reference_person  # Full name of reference person
        self.reference_contact = reference_contact  # Contact info as a dict {'mobile': '', 'email': ''}
        self.invoice_email = invoice_email  # Email address for invoices
        self.related_users = related_users if related_users else []  # List of user IDs
        self.customer_db = customer_db  # Path to CSV file for storing customer data

    @staticmethod
    def init_db(path: str):
        """
        Initialize the CSV file with headers.

        """
        with open(path, "w", newline="") as output_db:
            csv_writer = csv.writer(output_db)
            csv_writer.writerow([
                "customer_id", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])

    @staticmethod
    def save_to_csv(private_customers, path: str):
        """
        Save multiple private customer objects to the CSV file.

        """
        with open(path, "a", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "customer_id", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])
            for private_customer in private_customers:
                csv_writer.writerow(PrivateCustormer.__dict__)

    @staticmethod
    def read_csv_file(path: str):
        """
        Read and print the contents of the CSV file.

        """
        try:
            print("Opening the file...")
            with open(path, "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=",")
                # Read header
                header = next(csv_reader, None)  
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
        Remove a specific private customer entry from the CSV file based on customer_id.

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
                    print(f"Private customer entry with customer_id {customer_id} has been removed.")
            else:
                print(f"No private customer entry was found with customer_id {customer_id}")
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    @staticmethod
    def update_csv(path: str, customer_id: str, updated_data: dict):
        """
        Update a specific private customer entry in the CSV file based on customer_id.

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
                    print(f"Private customer entry with customer_id {customer_id} was updated.")
            else:
                print(f"No private customer entry was found with customer_id {customer_id}")

        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")
