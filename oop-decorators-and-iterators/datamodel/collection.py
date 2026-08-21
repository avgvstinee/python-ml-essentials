
# By implementing the corresponding special methods, a new type can emulate a built-in collection type the works well in a Pythonic style.

from collections import namedtuple

Item = namedtuple('Item', "name quantity")


class ShoppingList:
    def __init__(self,items): # initialize 
        self.items = items
        self.names = [name for (name,_) in items] # list of names
    
    def __getitem__(self, index): # get item by index
        return self.items[index]
    
    def __len__(self): # get length of the collection
        return len(self.items)
    
    def __iter__(self): # iterate over the collection
        return iter(self.items)
    
    def __contains__(self, name): # check if item is in the collection
        return name in self.names
    

milk = Item("Milk", 1)
banana = Item("Banana", 5)
bread = Item("Bread", 2)
my_list = ShoppingList([milk, banana, bread])

print(my_list[0])  # Item(name='Milk', quantity=1)

for item in my_list:
    print(item)  # print each item

print(f"There are {len(my_list)} items.")  # There are 3 items.

has_milk = "Milk" in my_list
has_chip = "Chip" in my_list
print(has_milk, has_chip)  # True False


