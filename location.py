class Location:
    
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __str__(self):
        """
        Return a string representation of the location.
        """
        return f"{self.city}, {self.country}"
