from django.test import TestCase
from restaurant.models import menu
from restaurant.serializers import MenuSerializer

class MenuItemTest(TestCase):
     def test_get_item(self):
        item = menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class MenuViewTest(TestCase):
       def setUp(self):
          self.menu_item1 = menu.objects.create(Title="IceCream", Price=80, Inventory=100)
          self.menu_item2 = menu.objects.create(Title="Cake", Price=150, Inventory=50)
          self.menu_item3 = menu.objects.create(Title="Coffee", Price=60, Inventory=200)

       def test_getall(self):
            menu_items=menu.objects.all()
            serializer=MenuSerializer(menu_items,many=True)
            data=serializer.data

            expected_data = [
            { 'Title': "IceCream", 'Price': '80.00', 'Inventory': 100},
            { 'Title': "Cake", 'Price': '150.00', 'Inventory': 50},
            { 'Title': "Coffee", 'Price': '60.00', 'Inventory': 200}
            ]
        
      
            self.assertEqual(data, expected_data)


    
