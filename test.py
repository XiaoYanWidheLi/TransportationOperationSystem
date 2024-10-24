import main_control_panel
from corporate import Corporate
from private_customer import PrivateCustomer

"""
main_control_panel.add_remove_update_user(action='a',name="Alice Johnson",
                                          address="123 Elm St, Springfield, IL 62704",
                                          phone= "832-456-1234", email="alice@example.com")

main_control_panel.add_remove_update_user(action='a',name="Michael Brown",
                                          address="321 Birch Rd, Seattle, WA 98101",
                                          phone= "123-789-4561", email="m.brown@example.com")

                                          adef add_remove_update_corporate():
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

"""  