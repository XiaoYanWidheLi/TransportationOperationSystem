import csv
import random
import string
import traceback

class User:
    """
    A class to represent a User.
    
    Attributes:
    -----------
    user_id : int
        A unique identifier for each user.
    full_name : str
        The full name of the user.
    address : str
        The residential address of the user.
    mobile_number : str
        The mobile contact number of the user.
    email : str
        The email address of the user.
    password : str
        The password for the user account. If not provided, a random one will be generated.
    """

    # Class variable shared by all instances
    user_id = 123_000
    def __init__(self, full_name, address, mobile_number, email, password= None):
        """
        Initialize a new User instance and auto-increment user_id for each new user.
        """
        # Increment the class-level user_id
        User.user_id += 1
        # Assign the incremented value to the instance
        self.user_id = User.user_id
        self.full_name = full_name
        self.address = address
        self.mobile_number = mobile_number      
        self.email = email
        self.password = password or self.generate_password()

    @classmethod    
    def generate_password(self):
        """Generate a random password"""
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def to_dict(self):
        """ Convert user data to a dictionary including user_id"""
        return {
            "user_id": self.user_id,
            "full_name": self.full_name,
            "address": self.address,
            "mobile_number": self.mobile_number,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def save_users_to_csv(users, path: str):
        """
        Save a list of User instances to a CSV file, including user_id.
        """
        with open(path, "w", newline="") as file:
            # Define the field names including 'user_id'
            fieldnames = ["user_id", "full_name", "address", "mobile_number", "email", "password"]
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for user in users:
                csv_writer.writerow(user.to_dict())
                print(f"User {user.user_id} {user.full_name} be added succesfully")

    @staticmethod
    def update_csv_file(path: str, user_id: str, updated_data: dict):
        """
        Update a specific user in the CSV file based on user_id.
        """
        try:
            # Read the CSV file
            with open(path, "r", newline="") as f:
                rows = list(csv.DictReader(f))
            
            # Print keys to debug and confirm correct field names
            print("CSV Headers:", rows[0].keys())

            updated = False
            # Use the parameter 'user_id' to match the correct row
            for row in rows:
                if "user_id" in row and row["user_id"] == user_id:  # Match user_id correctly
                    row.update(updated_data)
                    updated = True
                    break

            # Write back to the file only if an update was made
            if updated:
                with open(path, "w", newline="") as file:
                    if rows:  # Ensure that rows are not empty
                        csv_writer = csv.DictWriter(file, fieldnames=rows[0].keys())  # Dynamically retrieve headers
                        csv_writer.writeheader()
                        csv_writer.writerows(rows)
                        print(f"User with user_id {user_id} was updated.")
                    else:
                        print("Data not exist in the file, no rows to read and write.")
            else:
                print(f"No user with user_id {user_id} found.")
                
        except FileNotFoundError:
            print(f"Error: The file '{path}' does not exist.")
        except Exception as e:
            print(f"Error occurred: {e}")
            traceback.print_exc()

    @staticmethod
    def remove_users_from_csv(path:str, user_id:str):
        """
        Remove a specific user from he CSV file base on user_id.
        """
        try:
            # Read the CSV file.
            with open(path, "r", newline="") as f:
                rows = list(csv.DictReader(f))
                # Use the parameter"user_id" to sorted rows and save the row that no need remove in a new list.
                new_rows = [row for row in rows if "user_id" in row and row["user_id"] != user_id]

            # Write back the new_rows that will not remove to the csv file.
            with open(path,"w", newline="") as f:
                csv_writer=csv.DictWriter(f, fieldnames=rows[0].keys())
                csv_writer.writeheader()
                csv_writer.writerows(new_rows)
            print(f"User {user_id} has been succesfully removed.")
        except FileNotFoundError:
            print(f"Erro: File {path} not find.")
        except Exception as e:
            print(f"Erro accured {e}")


# Create some example users and save them to a CSV
users = [
    User("Alice Johnson", "123 Elm St, Springfield, IL", "832-456-1234", "alice@example.com"),
    User("Michael Brown", "321 Birch Rd, Seattle, WA", "123-789-4561", "m.brown@example.com")
]

# Save the users to a CSV file
User.save_users_to_csv(users, "users.csv")

updated_data = {
    "address": "Barytongatan 81",
    "mobile_number": "070-888-7777"
}

# Call the method to update the user with ID 123001
User.update_csv_file("users.csv", user_id="123001", updated_data=updated_data)

# Remove the user with ID 123002
User.remove_users_from_csv("users.csv", user_id = "123002")
