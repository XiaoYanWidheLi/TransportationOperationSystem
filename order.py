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
        self.order_id = f"ORD-{today}-{Order.order_counter:04d}"
        self.order_counter += 1

        self.priority = priority
        self.customer = customer
        self.delivery_location = delivery_location
        self.payment_details = payment_details
        self.items = []
        self.total_weight = 0
        self.order_status = order_status
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
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
        self.total_weight += item['weight']
        print(f"Item {item['name']} was added with weight {item['weight']}.")

    def to_dict(self):
        return{
            "order_id" : self.order_id,
            "priority" : self.priority,
            "customer" : self.customer,
            "delivery_location" : self.delivery_location,
            "payment_details" : self.payment_details,
            "items" : self.items,
            "total_weight" : self.total_weight,
            "order_status" : self.order_status,
            "order_date" : self.order_date, 
            "delivery_date" : self.delivery_date,
            "vehicle" : self.vehicle
        }

    def save_to_csv(self,path:str,orders:list):
        """
        Save the order details to a CSV file.
        """
        # Write to CSV
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file,fieldnames=["order_id", "priority", "customer",
                                                 "delivery_location", "payment_details",
                                                 "items", "total_weight", "order_status",
                                                "order_date", "delivery_date", "vehicle"])
            writer.writeheader()
            
            for row in orders:
                print(row.to_dict())
                writer.writerow(row.to_dict())
        print(f"Order {self.order_id} be added.")

    def __str__(self):
        """
        Return a string representation of the order details.
        """
        vehicle_info = self.vehicle.vehicle_id if self.vehicle else "No vehicle assigned"
        return (f"Order ID: {self.order_id}\n"
                f"Priority: {self.priority}\n"
                f"Customer: {self.customer}\n"
                f"Delivery Location: {self.delivery_location}\n"
                f"Items: {self.items}\n"
                f"Total Weight: {self.total_weight} kg\n"
                f"Order Status: {self.order_status}\n"
                f"Order Date: {self.order_date}\n"
                f"Delivery Date: {self.delivery_date}\n"
                f"Vehicle: {vehicle_info}\n")
    