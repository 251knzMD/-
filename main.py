from models import Item

# Create an item object
item1 = Item("Laptop", 10, 1200)
item1.display_info()
item1.add_stock(5)
item1.remove_stock(3)
item1.display_info()

item2 = Item("Office PC", 10, 1500)
item2.display_info()
item2.add_stock(1)
item2.remove_stock(2)
item2.display_info()

item3 = Item("Printer", 10, 600)
item3.display_info()
item3.add_stock(3)
item3.remove_stock(6)
item3.display_info()

item3 = Item("Printer Ink CMYK", 30, 60)
item3.display_info()
item3.add_stock(0)
item3.remove_stock(20)
item3.display_info()