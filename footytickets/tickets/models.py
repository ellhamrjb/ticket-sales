from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Tickets(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_soled= models.BooleanField(default=False)
    
        
    
