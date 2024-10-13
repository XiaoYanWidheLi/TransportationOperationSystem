import csv
import random
import string

class User:
    user_id = 123_000
    def __init__(self, full_name, address, mobile_number, email, password= None, user_db=None) -> None:
        User.user_id += 1
        self.full_name = full_name
        self.address = address
        self.mobile_number = mobile_number      
        self.email = email
        self.password= password
        self.user_db= user_db
        
    def generate_password(self):
        length = 12
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
    
    def __repr__(self) -> str:
        return f"User[ID: {self.user_id}, FullName: {self.full_name}, Address: {self.address}, Mobile: {self.mobile_number}, Email: {self.email}]"
    
    def create_csv_file(self,path:str,headers:dict):
        #Validate path and headers parameter
        path_ok = isinstance(path,str) and path.endswith('csv')
        headers_ok = isinstance(headers,dict)
        try:
            if path_ok and headers_ok:
                with open(path,mode='w',newline='') :
                    fieldnames = list(headers.keys())
                    csv_writer = csv.DictWriter(fieldnames=fieldnames,delimiter=',')
                    csv_writer.writeheader()
                    return True
            else:
                raise ValueError(f"[i] Bad value path = {path}")                   
        except Exception as error:
            raise error   

    def add_line_at_end(path:str, headers:dict ,line:dict):
        #Validate path and headers parameter
        path_ok = isinstance(path,str) and path.endswith('csv')
        header_ok = isinstance(headers,dict) \
                    and headers.keys() ==  line.keys()
        if path_ok and header_ok:
            #Validate columns of new line  match
            # those into the original file 
            columns = list()           
            try:            
                with open(path,mode='r') as csv_file:                    
                    csv_reader = csv.reader(csv_file,delimiter=',')
                    #get columns names of the file by reading first row
                    for row in csv_reader:
                        columns = row
                        break
                #print(f"columns = {columns}")
                if len(columns)==0:
                    raise ValueError(f"Bad Value no columns found , "+ \
                                     "run create_csv_file(path:str,headers:dict)\n")
            except Exception as error:
                        raise error
            # Once same columns in the original file nad the new line
            if columns == list(line.keys()):
                try:
                    with open(path,mode='a',newline='') as my_csv:
                        fieldnames = headers.keys()
                        csv_writer = csv.DictWriter(my_csv,delimiter=',',fieldnames=fieldnames)
                        csv_writer.writerow(line)
                        return True
                except Exception as error:
                    raise error
            else:
                raise ValueError(f"[i] Bad value line = {line}")
        else:
            raise ValueError(f"[i] Bad value path = {path}, header ={headers} nor line = {line}")      

user1 = User("001", "Alice Johnson",  "123 Elm St, Springfield, IL 62704",
"832-456-1234", "alice@example.com")

# Generate a random password
print(f"Generated password: {user1.generate_password()}")

# Create a CSV file
user1.create_csv_file(path="users.csv", headers=["full_name": {user1.full_name}, "address": user1.address, "mobile_number": user1.mobile_number, "email": user1.email, "password": user1.password])
