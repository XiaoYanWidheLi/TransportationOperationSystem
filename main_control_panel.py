from user import User
from corporate import Corporate
   
def display_menu():
        """Display the Operations for the Logistics System."""
        print("""
        ****** Main Control Panel ******
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
        *********************************
        """)

def add_remove_update_user(action=None, name=None, address=None, phone=None, email=None):
    #user1 = User(full_name="Alice Johnson", address="123 Elm St, Springfield, IL 62704",mobile_number="832-456-1234", email="alice@example.com")
    
    #user2 = User(full_name="Michael Brown", address="321 Birch Rd, Seattle, WA 98101",mobile_number="123-789-4561", email="m.brown@example.com")
    if action is None:
        action = input("(a)dd, (r)emove or (u)pdate user?")
    
    if name is None:
        name = input("Enter user name:")
    if address is None:
        address = input("Enter user address:")
    if phone is None:
        phone = input("Enter user phone number:")
    if email is None:
        email = input("Enter user email:")
        
#    user1 = User("Alice Johnson",  "123 Elm St, Springfield, IL 62704",
 #       "832-456-1234", "alice@example.com")
 #   user2 = User("Michael Brown", "321 Birch Rd, Seattle, WA 98101", "123-789-4561", "m.brown@example.com")
    user = User(name, address, phone, email)
    user.save_users_to_csv([user],"users.csv")
    #User.init_db("users.csv")  # Initialize user database
    #user_lines=[user1.to_dict(),user2.to_dict()]
    #User.add_lines_at_end(path="users.csv",
    #            headers={"full_name":"","address":"","mobile_number":"","email":"","password":""},
    #            lines=[user])

def main():
    # Change the variable name from 'Main_Control_Panel' to 'control_panel'
    # Create an instance of the Main_Control_Panel class
    #control_panel = Main_Control_Panel()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            # Add user
            add_remove_update_user()
        elif choice == '2':
                # Add corporate customer
            corporate1 = Corporate(
            customer_id="C001",  
            company_name="Tech Solutions Ltd.", 
            company_address="456 Pine St, San Francisco, CA 94111",
            reference_person="John Doe", 
            reference_contact="415-789-4567", 
            invoice_email="billing@techsolutions.com",
            related_users="john@example.com"
        )
            Corporate.init_db("corporate.csv")
            corporate1.save_to_csv(path="corporate.csv")
            corporate1.read_csv_file()
            
        elif choice == '3':
            pass
            

        elif choice == '4':
            pass

        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()