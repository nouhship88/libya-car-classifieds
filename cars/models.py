from django.db import models

class Car(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('SUV', 'SUV'),
        ('Truck', 'Truck'),
        ('Coupe', 'Coupe'),
        ('Convertible', 'Convertible'),
        # Add other car types as needed
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    odometer = models.IntegerField()  # In kilometers or miles
    color = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50, choices=CAR_TYPES)
    location = models.CharField(max_length=255)  # City or location
    dealer = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # Link to the dealer (user)

    def __str__(self):
        return self.title
