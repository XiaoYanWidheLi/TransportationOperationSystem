class Order:

    def __init__(self, order_id, priority, customer, delivery_location, payment_details, items, order_date, delivery_date, vehicle=None, order_status="Processing", order_db="orders.csv"):
        
        self.order_id = order_id
        self.priority = priority
        self.customer = customer
        self.delivery_location = delivery_location
        self.payment_details = payment_details
        self.items = items
        self.total_weight = self.calculate_total_weight()
        self.order_status = order_status
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.vehicle = vehicle
        self.order_db = order_db

    def calculate_total_weight(self):
        """
        Calculate the total weight of all items in the order.
        Returns the total weight in kg.
        """
        return sum(item['weight'] for item in self.items)

    def update_status(self, new_status):
        """
        Update the status of the order.
        - new_status: New status of the order ('Delivered', 'Processing', 'Canceled').
        """
        valid_statuses = ["Delivered", "Processing", "Canceled"]
        if new_status in valid_statuses:
            self.order_status = new_status
            print(f"Order status updated to '{new_status}'.")
        else:
            print("Invalid status. Please choose from 'Delivered', 'Processing', or 'Canceled'.")

    def assign_vehicle(self, vehicle):
        """
        Assign a vehicle to the order.
        - vehicle: A Vehicle object to be assigned to this order.
        """
        self.vehicle = vehicle
        print(f"Vehicle '{vehicle.vehicle_id}' assigned to the order.")

    def save_to_csv(self):
        """
        Save the order details to a CSV file.
        """
        # Prepare the data to be written to the CSV
        data = [
            self.order_id,
            self.priority,
            self.customer,
            str(self.delivery_location),
            self.payment_details.transaction_id if self.payment_details else "N/A",
            self.total_weight,
            self.order_status,
            self.order_date.strftime("%Y-%m-%d %H:%M:%S"),
            self.delivery_date.strftime("%Y-%m-%d %H:%M:%S"),
            self.vehicle.vehicle_id if self.vehicle else "N/A"
        ]

        # Write to CSV
        with open(self.order_db, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
        print(f"Order {self.order_id} saved to {self.order_db}.")

    def __str__(self):
        """
        Return a string representation of the order details.
        """
        vehicle_info = self.vehicle.vehicle_id if self.vehicle else "No vehicle assigned"
        return (f"Order ID: {self.order_id}\n"
                f"Priority: {self.priority}\n"
                f"Customer: {self.customer}\n"
                f"Delivery Location: {self.delivery_location}\n"
                f"Total Weight: {self.total_weight} kg\n"
                f"Order Status: {self.order_status}\n"
                f"Order Date: {self.order_date}\n"
                f"Delivery Date: {self.delivery_date}\n"
                f"Vehicle: {vehicle_info}\n")

# Example usage
# Assume Location, PaymentDetails, and Vehicle classes are defined as per the previous examples.
from datetime import datetime

# Example location, payment, and vehicle objects
delivery_location = Location(city="Stockholm", country="Sweden")
payment_details = PaymentDetails(payment_method="Credit Card", transaction_id="TXN12345", amount="200 €", payment_status="Paid", card_information={'card_number': '1234567812345678', 'cardholder_name': 'John Doe'})
vehicle = Vehicle(vehicle_id="Truck001", vehicle_type="truck", current_position=delivery_location, vehicle_db="vehicle_db.csv")

# List of items for the order
items = [
    {'name': 'Laptop', 'weight': 2},
    {'name': 'Monitor', 'weight': 7},
    {'name': 'Keyboard', 'weight': 1}
]

# Create an order
order = Order(
   
