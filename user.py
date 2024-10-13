import csv
import random
import string

class User:
    user_id = 123_000
    def __init__(self, full_name, address, mobile_number, email, password= None):
        User.user_id += 1
        self.full_name = full_name
        self.address = address
        self.mobile_number = mobile_number      
        self.email = email
        self.password = password or self.generate_password()
        
    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def __repr__(self) -> str:
        return f"User[ID: {self.user_id}, FullName: {self.full_name}, Address: {self.address}, Mobile: {self.mobile_number}, Email: {self.email}]"
    
    # def create_csv_file is from Ammars code:
    @staticmethod
    def create_csv_file(path: str, headers: list):
        """Create a new CSV file with the given headers."""
        path_ok = isinstance(path, str) and path.endswith('csv')
        headers_ok = isinstance(headers, dict)
        try:
            if path_ok and headers_ok:
                with open(path, mode='w', newline='') as csv_file:
                    csv_writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter=',')
                    csv_writer.writeheader()
                    print(f"CSV file '{path}' created successfully with headers: {headers}")
                    return True
            else:
                raise ValueError(f"[i] Bad value path = {path}")                   
        except Exception as error:
            raise error

    @staticmethod
    def add_lines_at_end(path: str, headers: dict, lines: list):
        """Adds multiple lines to the specified CSV file."""
        path_ok = isinstance(path, str) and path.endswith('csv')
        lines_ok = isinstance(lines, list)
        
        # Ensure all lines are dictionaries with the same keys as headers
        all_dict = all(isinstance(line, dict) and line.keys() == headers.keys() for line in lines)
        
        if path_ok and lines_ok and all_dict:
            try:
                # Validate columns by reading the existing CSV file's first row
                with open(path, mode='r') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    columns = next(csv_reader, None)  # Get the first row (header)
                    if not columns:
                        raise ValueError("Bad Value: No columns found. Run create_csv_file(path, headers).")
                    
                # Check that the file's existing columns match the header keys
                if columns != list(headers.keys()):
                    raise ValueError(f"[i] Bad value: CSV columns = {columns}, expected headers = {list(headers.keys())}")
                
                # Open the file in append mode and write all lines at once
                with open(path, mode='a', newline='') as my_csv:
                    fieldnames = headers.keys()
                    csv_writer = csv.DictWriter(my_csv, delimiter=',', fieldnames=fieldnames)
                    
                    # Write each line to the CSV file
                    csv_writer.writerows(lines)
                    print(f"CSV file '{path}' added successfully with lines: {lines}")
                    return True
                
            except Exception as error:
                raise error
        else:
            raise ValueError(f"[i] Bad value path = {path} or headers do not match lines")
        
    def to_dict(self):
        return{
            "full_name" : self.full_name,
            "address" : self.address,
            "mobile_number" : self.mobile_number,
            "email" : self.email,
            "password" : self.password
        }


user1 = User("Alice Johnson",  "123 Elm St, Springfield, IL 62704",
             "832-456-1234", "alice@example.com")
user2 = User("Michael Brown", "321 Birch Rd, Seattle, WA 98101", "123-789-4561", "m.brown@example.com")

user_lines=[user1.to_dict(),user2.to_dict()]

# Generate a random password
print(f"Generated password: {user1.generate_password()}")

# Create a CSV file
User.create_csv_file(path="users.csv", headers={"full_name":"","address":"","mobile_number":"","email":"","password":""})
User.add_lines_at_end(path="users.csv",
                      headers={"full_name":"","address":"","mobile_number":"","email":"","password":""},
                      lines=user_lines)
