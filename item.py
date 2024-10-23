class Item:

    def __init__(self, price_per_kg, volume, weight, is_fragile = False):
        # Price per kg (float)
        self.price_per_kg = price_per_kg
        # Volume in cubic meters (float)
        self.volume = volume 
        # Weight in kilograms (float)  
        self.weight = weight  
        # Type (e.g., fragile, solid)
        self.is_fragile = is_fragile
