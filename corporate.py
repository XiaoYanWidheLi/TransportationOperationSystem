import csv
import traceback

class Corporate:

    def __init__(self, customer_id, company_name, company_address, reference_person, reference_contact, 
                 invoice_email, related_users=None, customer_db="corporate.csv") -> None:
        self.customer_id = customer_id  # Unique identifier (e.g., organizational number or VAT number)
        self.company_name = company_name  # Official company name
        self.company_address = company_address  # Address as a dict {'street': '', 'building_no': '', 'zip_code': '', 'city': ''}
        self.reference_person = reference_person  # Full name of reference person
        self.reference_contact = reference_contact  # Contact info as a dict {'mobile': '', 'email': ''}
        self.invoice_email = invoice_email  # Email address for invoices
        self.related_users = related_users if related_users else []  # List of user IDs
        self.customer_db = customer_db  # Path to CSV file for storing customer data

    @staticmethod
    def init_db(path: str):
        """Initialize the CSV file with headers."""
        with open(path, "w", newline="") as output_db:
            csv_writer = csv.writer(output_db)
            csv_writer.writerow([
                "customer_id", "company_name", "company_address", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])

    @staticmethod
    def save_to_csv(corporates, path: str):
        """Save multiple corporate objects to the CSV file."""
        with open(path, "a", newline="") as file:
            csv_writer = csv.DictWriter(file, fieldnames=[
                "customer_id", "company_name", "company_address", "reference_person", "reference_contact", 
                "invoice_email", "related_users", "customer_db"
            ])
            for corporate in corporates:
                csv_writer.writerow(corporate.__dict__)

    @staticmethod
    def read_csv_file(path: str):
        """Read and print the CSV file."""
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
    def remove_from_csv(path:str,customer_id:str):
        """
        remove a specific corporate entry from csv file based on customer_id
        """
        try:
            # Read the file content.
            with open(path,"r") as file:
                csv_reader=csv.DictReader(file)
                rows=list(csv_reader)
                # Filter out the row that matches the given customer_id
                new_rows=[row for row in rows if row["customer_id"]!= customer_id]

            if len(new_rows) < len(rows):
                # Write the update list of rows back to the csv file    
                with open(path,"w") as f:
                    csv_writer=csv.DictWriter(f,fieldnames=csv_reader.fieldnames)
                    csv_writer.writeheader()
                    csv_writer.writerows(new_rows)
                    print(f"Corporate entry with customer_id {customer_id} has been removed.")
            else:
                print(f"No corporate entry was found with customer_id {customer_id}")
        except FileNotFoundError:
            print(f"Erro: The file '{path}' does not exist.")
        except Exception as e:
            print(f"An erro accured: {e}")
    @staticmethod
    def update_csv(path:str,customer_id:str,updated_data:dict):
        """
        Update a specific corporate entry in csv file based on customer_id.
        The update_data dictionary should contain the fields to be updated and their new values

        """
        try:
            # Read the csv file
            with open(path,"r",newline="") as f:
                rows=list(csv.DictReader(f))

            # Update the record that match the customer_id
            updated = False
            for row in rows:
                if row["customer_id"]==customer_id:
                    row.update(updated_data)
                    updated = True
                    break
            
            # If the matching record was found, write the updated rows back to the csv file.
            if updated:
                with open(path,"w",newline="") as f:
                    # rows[0].keys() or row.keys() provides the column headers for the CSV file
                    # dynamically retrieves the column headers (keys of the dictionary) from the first row in the CSV file
                    csv_writer = csv.DictWriter(f,fieldnames=rows[0].keys())
                    csv_writer.writeheader()
                    csv_writer.writerows(rows)
                    print(f"Corporate entry with customer_id {customer_id} was updated")
            else:
                print(f"No corporate entry was found with customer_id {customer_id}")

        except FileNotFoundError:
            print(f"Erro: The file {path} does not exist ")
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
        related_users="jane@example.com"
    ),
    Corporate(
        customer_id="C002",  
        company_name="Tech Solutions Ltd.", 
        company_address="456 Pine St, San Francisco, CA 94111",
        reference_person="John Doe", 
        reference_contact="415-789-4567", 
        invoice_email="billing@techsolutions.com",
        related_users="john@example.com"
    )
]

# Initialize the CSV file
Corporate.init_db("corporate.csv")

# Save the corporate objects to the CSV file
Corporate.save_to_csv(corporates, path="corporate.csv")

# Read the CSV file to verify the content
Corporate.read_csv_file("corporate.csv")

#Corporate.remove_from_csv("corporate.csv",customer_id="C001")

# Update the corporate entry with customer_id "C002"
updated_data={
    "company_name": "Tourism Innovations Ltd.",
    "invoice_email": "babal@techinnovations.com"
}
Corporate.update_csv("corporate.csv",customer_id="C002",updated_data=updated_data)