from django.db import models

# Create your models here.
class booking(models.Model):
    #ID=models.IntegerField(primary_key=True)
    Name=models.CharField(max_length=200)
    No_of_guests=models.IntegerField()
    BookingDate=models.DateTimeField()

    

class menu(models.Model):
     #ID=models.IntegerField(primary_key=True)
     Title=models.CharField(max_length=255)
     Price=models.DecimalField(max_digits=(10),decimal_places=(2))
     Inventory=models.IntegerField()

     def __str__(self):
        return f'{self.Title} : {str(self.Price)}'


