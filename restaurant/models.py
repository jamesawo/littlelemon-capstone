from django.db import models

class Menu(models.Model):
   title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=10, decimal_places=2) 
   inventory = models.PositiveSmallIntegerField() 

   def __str__(self):
      return f'{self.title} : {str(self.price)}'

class Booking(models.Model):
    name = models.CharField(max_length=255)
    number_of_guests = models.PositiveSmallIntegerField()
    booking_date = models.DateTimeField()

    def __str__(self): 
        return f'{self.name} : {self.number_of_guests} : {self.booking_date}'
