import csv

class Vehicle:
    bike_id = 1
    truck_id = 1
    ship_id = 1
    valid_statuses = ['free', 'busy', 'loading', 'not working']
    """
        Initialize a Vehicle object.
        - vehicle_id: Unique ID for the vehicle.
        - max_capacity_weight: Maximum weight capacity in kg.
        - Remaining Capacity: Remaining weight capacity (kg) and item capacity
        - current_position: Initial position of the vehicle.
        - vehicle_db: Path to the CSV file containing vehicle data.
        - status: Vehicle status, default is 'free'.
        """
    def __init__(self, vehicle_type, status, current_location):
        self.vehicle_type = vehicle_type
        self.status = status
        self.current_location = current_location
        self.vehicle_id = self.generate_vehicle_id()
        self.max_capacity()
        self.current_items = 0
        self.current_weight = 0
    
    def generate_vehicle_id(self):
        """
        generate a unique vehicle ID base on the type of vehicle.
        """
        prefix = ""
        if self.vehicle_type == "Bike":
            prefix = "B"
            new_id = f"{prefix}{str(Vehicle.bike_id).zfill(3)}"
            Vehicle.bike_id += 1
        elif self.vehicle_type == "Truck":
            prefix = "T"
            new_id = f"{prefix}{str(Vehicle.truck_id).zfill(3)}"
            Vehicle.truck_id += 1
        elif self.vehicle_type == "Ship":
            prefix = "SH"
            new_id = f"{prefix}{str(Vehicle.ship_id).zfill(3)}"
            Vehicle.ship_id += 1
        
        return new_id
    
    @staticmethod
    def vehicle_selection(items, weight):
        if 0 < items <= 2 and 0 < weight <= 10:
            print(f"With {items} items and {weight} KG weight suitable load with bike")
            return "Bike"
        
        elif 0 < items <= 100 and 0 < weight <= 3000:
            print(f"With {items} items and {weight} KG weight suitable load with truck")
            return "Truck"
        elif 0 < items <= 10000 and 0 < weight <= 100000:
            print(f"With {items} items and {weight} KG weight suitable load with ship")
            return "Ship"
        
    def max_capacity(self):
        """
        Set vehicle-specific capacity limits based on the type of vehicle.
        """
        if self.vehicle_type =="Bike":
           self.max_capacity_items = 2
           self.max_capacity_weight = 10
        elif self.vehicle_type == "Truck":
           self.max_capacity_items = 100
           self.max_capacity_weight = 3000
        elif self.vehicle_type == "Ship":
            self.max_capacity_items = 10000
            self.max_capacity_weight = 100000

    def load_items (self,items, weight):
        """Attempt load items onto the vehicle and update the current capacity."""
        
        if self.current_items + items > self.max_capacity_items or self.current_weight + weight > self.max_capacity_weight:
            print(f"Capacity not enough. {items} items {weight} kg can not be load onto {self.vehicle_type} {self.vehicle_id}")
        else:
            self.current_items += items
            self.current_weight += weight
            print(f"Load {items} items ({weight} Kg) onto the {self.vehicle_type} {self.vehicle_id}")
        return self.current_items, self.current_weight
    def remaining_capacity(self):
        """
        Calculate remaining capacity based on current items and weight.
        """
        remaining_capacity_items = self.max_capacity_items - self.current_items
        remaining_capacity_weight = self.max_capacity_weight - self.current_weight
        print(f"{self.vehicle_type} {self.vehicle_id} remaining capacity {remaining_capacity_items} items, {remaining_capacity_weight} kg")
        return remaining_capacity_items, remaining_capacity_weight
    """
    def update_position(self, city, country):
    
        #Update the vehicle's current position.
        update_position = f"{city} {country}" 

        # Update the vehicle's current location
        self.current_position = update_position
        print(f"Vehicle position updated to {update_position}.")
        # Update the vehicle's current location
    """
    @staticmethod
    def save_to_csv(vehicles, path:str):
        """
        Save the vehicle's current state to the CSV file.
        Accepts either a single Vehicle object or a list of Vehicle objects.
        """
        # Checks if vehicles is a single Vehicle object.
        if isinstance(vehicles, Vehicle):
            #Turns that single object into a list containing that object.
            vehicles = [vehicles]

        fieldnames=["vehicle_id", "vehicle_type", "status", "current_location"]
        with open(path,"w",newline="") as f:
            csv_writer = csv.DictWriter(f,fieldnames=fieldnames )
            
            # Write header only if file is empty
            if f.tell() == 0:
                csv_writer.writeheader()
            
            # Write each vehicle's data as a row
            for vehicle in vehicles:
                csv_writer.writerow({
                    "vehicle_id" : vehicle.vehicle_id,
                    "vehicle_type": vehicle.vehicle_type,
                    "status" : vehicle.status,
                    "current_location": vehicle.current_location
                })
                print(f"{vehicle.vehicle_type} with ID {vehicle.vehicle_id} be added to system succesfully.")


"""
     Vehicle Selection Task (40 points):
     Create a function to select the correct and available vehicle for a shipment.
     Test it with the following scenarios:
     • Shipment 1: 1 item, total weight 5 kg
     • Shipment 2: 12 items, total weight 3 kg
     • Shipment 3: 60 items, total weight 4,500 kg
     • Shipment 4: 120 items, total weight 2,500 kg"""

# Vehicle selection
Vehicle.vehicle_selection(1,5)
Vehicle.vehicle_selection(12,3)
Vehicle.vehicle_selection(60,4500)
Vehicle.vehicle_selection(120,2500)

# Add a bike to the system
bike_1 = Vehicle(vehicle_type="Bike", status = "available",current_location= "goteborg, Sweden")
bike_2 = Vehicle(vehicle_type="Bike", status="available", current_location="malmo, Sweden")
bike_3 = Vehicle(vehicle_type="Bike", status="available", current_location="stockholm, Sweden")
# Add a truck to the system. 
truck_1 = Vehicle(vehicle_type="Truck", status = "available", current_location= "Beijing, Kina")
truck_2 = Vehicle(vehicle_type="Truck", status="available", current_location="Shanghai, Kina")
truck_3 = Vehicle(vehicle_type="Truck", status="available", current_location="Chengdu, Kina")
# Add a ship to the system. 
ship_1 = Vehicle(vehicle_type="Ship", status= "available", current_location= "London, Uk")
ship_2 = Vehicle(vehicle_type="Ship", status="available", current_location="Liverpool, Uk")
ship_3 = Vehicle(vehicle_type="Ship", status="available", current_location="New York, USA")

# Load items onto a vehicle.
bike_1.load_items(1,5)
bike_1.load_items(2,7)
# check remaining capacity.
bike_1.remaining_capacity()

# Print the vehicle IDs to verify they are generated correctly
print(bike_1.vehicle_id)      
print(bike_2.vehicle_id)  
print(bike_3.vehicle_id)  

print(truck_1.vehicle_id) 
print(truck_2.vehicle_id) 
print(truck_3.vehicle_id)  

print(ship_1.vehicle_id) 
print(ship_2.vehicle_id) 
print(ship_3.vehicle_id)


Vehicle.save_to_csv([bike_1,bike_2], "vehicles.csv")

