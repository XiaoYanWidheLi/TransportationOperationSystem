from datetime import datetime
import csv

class Order:
    """
    Generate oreder_id based on Date and Counter,making it more traceable.
    """
    current_time = datetime.now().strftime("%Y%m%d")
    order_counter = 1

    def __init__(self, priority, customer, delivery_location, payment_details, order_status="Processing"):
        today = datetime.now().strftime("%Y%m%d")
        if Order.current_time != today:
            Order.current_time = today
            Order.order_counter = 1
        # Generate the order ID
        self.order_id = f"ORD-{today}{Order.order_counter:4d}"
        self.order_counter += 1

        self.priority = priority
        self.customer = customer
        self.delivery_location = delivery_location
        self.payment_details = payment_details
        self.items = []
        self.total_weight = 0
        self.order_status = order_status
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.delivery_date = None
        self.vehicle = None

    def update_status(self, new_status):
        """
        Update the status of the order.
        - new_status: New status of the order ('Delivered', 'Processing', 'Canceled').
        """
        valid_statuses = ["Delivered", "Processing", "Canceled"]
        if new_status in valid_statuses:
            self.order_status = new_status
            print(f"Order {self.order_id} status updated to '{self.order_status}'.")
        else:
            raise ValueError(f"Invalid status. Please choose from {valid_statuses}.")

    def get_status(self):
        """
        Retrieve the current status of the order.
        """
        return self.order_status

    def add_items(self, item):
        self.items.append(item)
        self.total_weight += item.weight
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

# List of items for the order
items = [
    {'name': 'Laptop', 'weight': 2},
    {'name': 'Monitor', 'weight': 7},
    {'name': 'Keyboard', 'weight': 1}
]

# Create an order
order = Order(priority="Medium", customer="Alice Smith", delivery_location="456 Oak Ave",
              payment_details="PayPal")

# Print initial status
print(f"Initial Order Status: {order.get_status()}")  # Output: Initial Order Status: Processing

# Update the order status to Delivered
order.update_status("Delivered")

# Retrieve the updated status
print(f"Updated Order Status: {order.get_status()}")  # Output: Updated Order Status: Delivered
