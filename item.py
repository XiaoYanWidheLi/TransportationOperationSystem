class Item:

    def __init__(self, price_per_kg, volume, weight, item_type):
        # Price per kg (float)
        self.price_per_kg = price_per_kg
        # Volume in cubic meters (float)
        self.volume = volume 
        # Weight in kilograms (float)  
        self.weight = weight  
        # Type (e.g., fragile, solid)
        self.item_type = item_type  
        
    def volume(self,length, width, height):
        """
        Calculate the volume based on length, width, and height.
        """
        # Length in meters (float)
        self.length = length
        # Width in meters (float)
        self.width = width  
        # Height in meters (float)
        self.height = height  

        return self.length * self.width * self.height

    def shipping_cost(self):
        """
        Calculate shipping cost based on the weight and price per kg.
        """
        return self.price_per_kg * self.weight

    def is_fragile(self):
        """
        Checks if the item is fragile.
        Returns True if the item type is 'fragile'.
        """
        return self.item_type == 'fragile'

