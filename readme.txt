Librabies Used
================

- import Item class into main.py.
- print()
- class
- methods
- my meds

How to use
================
Copy and paste in code for new items in file main.py

run code by pressing the run button on top of your software or with a shortcut.
Current known Shortcuts:
/Shift+F10/PyCharm/
/F5/VS Code/

item1 = Item("Laptop", 10, 1200) ## Item("Name", Starting Quantity, Price).
item1.display_info() ## Displays the curent item and its quantity as well as it's changes and thе final(changed) info about the item.
item1.add_stock(5) ## Change number to how many you want to add
item1.remove_stock(3) ## Change number to how many you want to remove
item1.display_info() ## Display final version. Item("Name", New Quantity, Price).



Как се ползва
================
Копирайте и поставете кода за нови елементи във файла main.py. 

Стартирайте кода, като натиснете бутона за изпълнение в горната част на софтуера или с бърз клавиш. 
Текущи известни бързи клавиши:
/Shift+F10/PyCharm/
/F5/VS Code/

item1 = Item("Laptop", 10, 1200) ## Item("Име", начално количество, Цена).
item1.display_info() ## Показва текущия артикул и неговото количество и цена, промените в него и окончателната (променена) информация за артикула.
item1.add_stock(5) ## Колко да бъдад добавени
item1.remove_stock(3) ## Колко да бъдад премахнати
item1.display_info() ## Показва окончателната версия. Item("Име", актуална наличност, Цена).