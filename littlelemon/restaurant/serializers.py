from rest_framework import serializers
from .models import menu,booking
class MenuSerializer(serializers.ModelSerializer):
     Price = serializers.DecimalField(max_digits=10, decimal_places=2)  # Decimal with 2 decimal places
     Inventory = serializers.IntegerField()
     class Meta:
        model=menu
        fields=['Title','Price','Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=booking
        fields=['Name','No_of_guests','BookingDate']
