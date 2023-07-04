"""
Assessment 3.1 - Inventory Class

Write an "Inventory" class, as defined below, that handles the management of inventory for a company. All instances of this class should be
initialized by passing an integer value named "max_capacity" that indicates the maximum number of items that can be stored in inventory.
Your "Inventory" class will need to store items that are represented by a "name", "price" and "quantity".

Your class should implement the following methods:

- add_item(name, price, quantity): This method should add an item to inventory and return "True" if it was successfully added. If adding
an item results in the inventory being over capacity your method should return "False" and omit adding this item to the inventory. 
Additionally, if an item with the passed name already exists in inventory this method should return "False" to indicate the item could 
not be added.

- delete_item(name): This method should delete an item from inventory and return "True" if the item was successfully deleted. If there is
no item with the passed "name" this method should return "False".

- get_most_stocked_item(): This method should return the name of the item that has the highest quantity in the inventory, and return "None"
if there are no items in the inventory. You may assume there will always be exactly one item with the largest quantity, except for the case
where the inventory is empty.

- get_items_in_price_range(min_price, max_price): This method should return a list of items that have a price within the specified range 
(inclusively).

Note: you may assume all input/arguments to your class will be valid and the correct types. For example, the max_capacity will always be 
greater than or equal to 0 and a valid integer.
"""

class Inventory:
    def __init__(self, max_capacity):
        # Write your code here.
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        # Write your code here.

        # Returns False if item already exists in inventory:
        if name in self.items:
            return False
        
        # Returns False if item quantity exceeds max. capacity:
        if self.item_count + quantity > self.max_capacity:
            return False

        # Adds an item to inventory and returns True if it was successfully added:
        self.items[name] =  {"name": name, "price": price, "quantity": quantity}
        self.item_count += quantity
        return True
        

    def delete_item(self, name):
        # Write your code here.

        # Returns False if item does not exist in inventory:
        if name not in self.items:
            return False
        
        # Deletes an item from inventory and returns True if it was successfully deleted:
        self.item_count -= self.items[name]["quantity"]    # Subtracts the quantity of deleted element
        del self.items[name]                                # Deletes the name of element
        return True  

    def get_most_stocked_item(self):
        # Write your code here.
        most_stocked_item_name = None
        largest_quantity = 0

        for item in self.items.values():
            name = item["name"]
            quantity = item["quantity"]

            if quantity > largest_quantity:
                most_stocked_item_name = name
                largest_quantity = quantity
        
        return most_stocked_item_name
    
    def get_items_in_price_range(self, min_price, max_price):
        # Write your code here.
        item_names = []

        for item in self.items.values():
            name = item["name"]
            price = item["price"]

            if min_price <= price <= max_price:
                item_names.append(name)
        
        return item_names
