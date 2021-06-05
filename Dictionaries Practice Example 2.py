# Dictionary Tutorial #2
# Adapted from Automate the Boring Stuff With Python page 120 (List to Dictionary Function for Fantasy Game)
# Inventory

# Given an dictionary of goods and a list of loot, the task at hand is to update the
# dictionary with the added loot, and display the new dictionary

# Provided items
inventory = {'gold coin':42, 'rope':1}
loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

# Loop through the loot list
# For each item within loot, determine if it is an existing key within the
# dictionary inventory
# If not, add the item as an index in the dictionary and initiate its value as 0
# If it is, bypass the if statement
for item in loot:
    if item not in inventory:
        inventory[item] = 0

    # In either case, we need to increment the number of the item by 1.
    inventory[item] += 1

# Print the inventory
# .items() converts the dictionary into a list of tuples
# [(key1, value1), (key2, value2), ...]
# [('gold coin', 45), ('rope', 1), ...]
# The for statement below simultaneously loops through the keys and values together
# Keys: 'gold coin', 'rope', ...
# Values: 45, 1, ...
for key,value in inventory.items():
    # Remember that the print command only takes string as input
    print(str(value)+' '+key)


