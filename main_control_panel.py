from user import User
from corporate import Corporate
from vehicle import Vehicle
from order import Order
from private_customer import PrivateCustomer
   
def display_menu():
        """Display the Operations for the Logistics System."""
        print("""
        ****** Main Control Panel ******
        0. press Q/q To quite the programme
        1. Add/remove/update a user in the system
        2. Add/remove/update a corporate customer
        3. Add/remove/update a private customer
        4. Add a bike to the system
        5. Add a truck to the system
        6. Add a ship to the system
        7. Create a shipment/order
        8. Add items to a shipment
        9. Update the status of an order
        10. Retrieve the updated status of an order
        11. Vehicle selection
        *********************************
        """)

def add_remove_update_user(action=None, name=None, address=None, phone=None, email=None):
    #user1 = User(full_name="Alice Johnson", address="123 Elm St, Springfield, IL 62704",mobile_number="832-456-1234", email="alice@example.com")
    #user2 = User(full_name="Michael Brown", address="321 Birch Rd, Seattle, WA 98101",mobile_number="123-789-4561", email="m.brown@example.com")
    
    if action is None:
        action = input(("(a)dd, (r)emove or (u)pdate user?").lower())
        if action == 'a':
            
            if name is None:
                name = input("Enter user name:")
            if address is None:
                    address = input("Enter user address:")
            if phone is None:
                    phone = input("Enter user phone number:")
            if email is None:
                    email = input("Enter user email:")  
            # Create a User instance
            new_user = User(full_name=name, address=address, mobile_number=phone, email=email)  
            users = [new_user,]
            # Save the new user to the CSV file
            User.save_users_to_csv(users, "users.csv")
        elif action == 'r':
            # Display all users before asking for ID to remove
            print("Here is all the users: ")
            users = User.load_users_from_csv("users.csv")
            if not users:
                 print("No user was found, the list is empty.")
                 return
            for user in users:
                print(f"ID: {user.user_id}, Name: {user.full_name}, Address: {user.address}, Phone: {user.mobile_number}, Email: {user.email}")
            User.remove_users_from_csv("users.csv")
        elif action == 'u':
            # Display all users before asking for ID to remove
            print("Here is all the users: ")
            users = User.load_users_from_csv("users.csv")
            if not users:
                 print("No user was found, the list is empty.")
                 return
            for user in users:
                print(f"ID: {user.user_id}, Name: {user.full_name}, Address: {user.address}, Phone: {user.mobile_number}, Email: {user.email}")
            User.update_csv_file("users.csv")
def add_remove_update_corporate():
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

def add_remove_update_private_customer():

    # Initialize the CSV file
    PrivateCustomer.init_db("private_customers.csv")

    # Create two new customer instances
    customer1 = PrivateCustomer(
        customer_id="CUST001",
        reference_person="John Doe",
        reference_contact={"mobile": "123-456-7890", "email": "john.doe@example.com"},
        invoice_email="invoices@doe.com",
        related_users=["200001", "200002"]
    )

    customer2 = PrivateCustomer(
        customer_id="CUST002",
        reference_person="Jane Smith",
        reference_contact={"mobile": "987-654-3210", "email": "jane.smith@example.com"},
        invoice_email="invoices@smith.com",
        related_users=["200003",]
    )

    # Save both customers to the CSV file
    PrivateCustomer.save_to_csv([customer1, customer2], "private_customers.csv")


    # Read the customer.
    PrivateCustomer.read_csv_file("private_customers.csv")

    # Update the corporate entry with customer_id "C002"
    updated_info = {
    "reference_person": "Johnathan Doe",
    "invoice_email": "newinvoice@doe.com"
    }
    PrivateCustomer.update_csv("private_customers.csv", "CUST001", updated_info)

    # Remove a cusomer
    PrivateCustomer.remove_from_csv("private_customers.csv", "CUST001")


def add_truck():
     # Add a truck to the system. 
    truck_1 = Vehicle(vehicle_type="Truck", status = "available", current_location= "Beijing, Kina")
    truck_2 = Vehicle(vehicle_type="Truck", status="available", current_location="Shanghai, Kina")
    truck_3 = Vehicle(vehicle_type="Truck", status="available", current_location="Chengdu, Kina")

    print(truck_1.vehicle_id) 
    print(truck_2.vehicle_id) 
    print(truck_3.vehicle_id) 

    Vehicle.save_to_csv([truck_1,truck_2,truck_3], "trucks.csv")


def add_bike():
     # Add a bike to the system
    bike_1 = Vehicle(vehicle_type="Bike", status = "available",current_location= "goteborg, Sweden")
    bike_2 = Vehicle(vehicle_type="Bike", status="available", current_location="malmo, Sweden")
    bike_3 = Vehicle(vehicle_type="Bike", status="available", current_location="stockholm, Sweden")
    
    # Print the vehicle IDs to verify they are generated correctly
    print(bike_1.vehicle_id)      
    print(bike_2.vehicle_id)  
    print(bike_3.vehicle_id) 

    Vehicle.save_to_csv([bike_1,bike_2, bike_3], "bikes.csv")

    # Load items onto a vehicle.
    bike_1.load_items(1,5)
    bike_1.load_items(2,7)
    # check remaining capacity.
    bike_1.remaining_capacity()


def add_ship():
     # Add a ship to the system. 
    ship_1 = Vehicle(vehicle_type="Ship", status= "available", current_location= "London, Uk")
    ship_2 = Vehicle(vehicle_type="Ship", status="available", current_location="Liverpool, Uk")
    ship_3 = Vehicle(vehicle_type="Ship", status="available", current_location="New York, USA")

    print(ship_1.vehicle_id) 
    print(ship_2.vehicle_id) 
    print(ship_3.vehicle_id)

    Vehicle.save_to_csv([ship_1, ship_2, ship_3], "ships.csv")


def create_order():
     # Create an shipment
    order = Order(priority="Medium",
                customer="Alice Smith", 
                delivery_location="456 Oak Ave",
                payment_details="PayPal",
                )
    orders =[order,]

    order.save_to_csv("orders.csv",orders=orders)
    order.__str__()
def add_items_to_order():
     # Create an shipment
    order = Order(priority="Medium",
                customer="Alice Smith", 
                delivery_location="456 Oak Ave",
                payment_details="PayPal"
                )
    orders = [order,]
     # List of items for the order
    items = [
        {'name': 'Laptop', 'weight': 2},
        {'name': 'Monitor', 'weight': 7},
        {'name': 'Keyboard', 'weight': 1}
    ]
    for item in items:
        order.add_items(item)
    print(f"Items has been added to the shipment/order, and totle weight is: {order.total_weight}")
    order.save_to_csv("orders.csv",orders=orders)

def update_order_status():
     # Create an shipment
    order = Order(priority="Medium",
                customer="Alice Smith", 
                delivery_location="456 Oak Ave",
                payment_details="PayPal")
    
     # Print initial status
    print(f"Initial Order Status: {order.get_status()}")  # Output: Initial Order Status: Processing

    # Update the order status to Delivered
    order.update_status("Delivered")


def retrieve_status():
    # Create an shipment
    order = Order(priority="Medium",
                customer="Alice Smith", 
                delivery_location="456 Oak Ave",
                payment_details="PayPal")
     # Retrieve the updated status
    # Output: Updated Order Status: Delivered     
    print(f"Updated Order Status: {order.get_status()}")  


def vehicle_selection():
    Vehicle.vehicle_selection(1,5)
    Vehicle.vehicle_selection(12,3)
    Vehicle.vehicle_selection(60,4500)
    Vehicle.vehicle_selection(120,2500)


def main():
    # Change the variable name from 'Main_Control_Panel' to 'control_panel'
    # Create an instance of the Main_Control_Panel class
    #control_panel = Main_Control_Panel()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == 'q' or choice =='Q':
            print("Quite the Programe.")
            break
        elif choice == '1':
            # Add/remove/update a user in the system
            add_remove_update_user()
        elif choice == '2':
            add_remove_update_corporate()
        elif choice == '3':
            #Add/remove/update a private customer
            add_remove_update_private_customer()            
        elif choice == '4':
            # Add a bike to the system
            add_bike()
        elif choice == '5':
            # Add a truck to the system
            add_truck()
        elif choice == '6':
            # Add a ship to the system
            add_ship()
        elif choice == '7':
            # Create a shipment/order
            create_order()
        elif choice == '8':
            # Add items to a shipment
            add_items_to_order()
        elif choice == '9':
            # Update the status of an order
            update_order_status()
        elif choice == '10':
            # Retrieve the updated status of an order
            retrieve_status()
        elif choice == '11':
            # Vehicle selection
            vehicle_selection()
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()