class Vehicle:
    def __init__(self, vehicle_id, max_capacity_weight, max_capacity_items, current_position,
                  vehicle_db, status='free'):
        """
        Initialize a Vehicle object.
        - vehicle_id: Unique ID for the vehicle.
        - max_capacity_weight: Maximum weight capacity in kg.
        - max_capacity_items: Maximum number of items.
        - current_position: Initial position of the vehicle.
        - vehicle_db: Path to the CSV file containing vehicle data.
        - status: Vehicle status, default is 'free'.
        """
        self.vehicle_id = vehicle_id
        self.max_capacity_weight = max_capacity_weight
        self.max_capacity_items = max_capacity_items
        self.remaining_capacity_weight = max_capacity_weight
        self.remaining_capacity_items = max_capacity_items
        self.current_position = current_position
        self.status = status
        self.vehicle_db = vehicle_db

    def max_capacity(self):
        """
        Set vehicle-specific capacity limits based on the type of vehicle.
        """
        if self.vehicle_type == "bike":
            self.max_capacity_weight = 10  # Max weight capacity in kg for a bike
            self.max_capacity_items = 2    # Max item count for a bike
        elif self.vehicle_type == "truck":
            self.max_capacity_weight = 3000  # Max weight capacity in kg for a truck
            self.max_capacity_items = 100    # Max item count for a truck
        elif self.vehicle_type == "ship":
            self.max_capacity_weight = 100000  # Max weight capacity in kg for a ship
            self.max_capacity_items = 10000    # Max item count for a ship
        else:
            raise ValueError("Invalid vehicle type. Choose from 'bike', 'truck', or 'ship'.")
            
    def status(self, new_status):
        """
        Change the vehicle status.
        - new_status: Can be 'free', 'busy', 'loading', or 'not working'.
        """
        valid_statuses = ['free', 'busy', 'loading', 'not working']
        if new_status in valid_statuses:
            self.status = new_status
            print(f"Vehicle status changed to {new_status}.")
        else:
            print("Invalid status. Please choose from 'free', 'busy', 'loading', or 'not working'.")


    def remaining_capacity(self):
        pass

    def current_position(self, new_position):
        """
        Update the vehicle's current position.
        - new_position: New location of the vehicle.
        """
        self.current_position = new_position
        print(f"Vehicle position updated to {new_position}.")

    def vehicle_db(self):
        """
        Save the vehicle's current state to the CSV file.
        """
        pass