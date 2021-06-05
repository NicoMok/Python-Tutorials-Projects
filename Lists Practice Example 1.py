# List Tutorial #1
# Automate the Boring Stuff With Python page 114

allGuests = {'Alice': {'apples':5, 'pretzels':12},
             'Bob': {'ham sandwiches':3, 'apples':2},
             'Carol': {'cups':3, 'apple pies':1}}

# Create a function that determines the number of food items each
# person has brought

listOfItems = []
for name in allGuests.keys():
    # The extend method is used only for lists.
    # Adds the elements within the list allGuests[name].keys() to the
    # list listOfItems.
    # Note: using the append method does the same thing, but
    # adds 1 element, the list allGuests[name].keys(), to the
    # list listOfItems

    listOfItems.extend(allGuests[name].keys())

# Remove duplicates by changing the list into a set
listOfItems = set(listOfItems)

# Define a function that determines the total number of items brought
# to the field
def getNumberOfItems(allGuests, item):
    numberOfItem = 0

    for name in allGuests.keys():
        # The get method only works for lists.
        # It searches the list 'allGuests[name]' for a KEY of name
        # item.
        # It then returns the corresponding value if the key exists...
        # If the key item doesn't exist, it returns 0, as specified
        # by the second argument of the method.
        numberOfItem = numberOfItem + allGuests[name].get(item,0)

    return numberOfItem

# Loop through the list of items. Print the number of each item
for item in listOfItems:
    print(item + '   ' + str(getNumberOfItems(allGuests,item)))


