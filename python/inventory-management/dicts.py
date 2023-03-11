"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list.

    :param items: list - list of items to create an inventory from.
    :return: dict - the inventory dictionary.
    """
    dictionary = dict()
    for item in items:
        if item not in dictionary: 
            dictionary[item] = 1
        else:
            dictionary[item] += 1
    return dictionary

# print(create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`.

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return: dict - the inventory updated with the new items.
    """
    items_dict = create_inventory(items)
    res_dict = {item: items_dict.get(item, 0) + inventory.get(item, 0) for item in set(items_dict).union(inventory)}
    return res_dict

# print(add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list.

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return: dict - updated inventory with items decremented.
    """
    for item in items:
        if item in items:
            if inventory[item] > 0:
                inventory[item] -= 1
            else: 
                inventory[item] = 0
    return inventory

# print(decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
# print(decrement_items({"iron": 3, "diamond": 4, "gold": 2},["iron", "iron", "diamond", "gold", "gold"]))

def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string.

    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return: dict - updated inventory with item removed. Current inventory if item does not match.
    """
    if inventory.get(item) != None:
        del inventory[item]
    return inventory

print(remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))     


def list_inventory(inventory):
    """Create a list containing all (item_name, item_count) pairs in inventory.

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    inv_list = []
    for item in inventory.items():
        if item[1] > 0:
            inv_list.append(item)
    return inv_list
