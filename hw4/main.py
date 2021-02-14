"""
pirple/python/hw4/main.py
Homework Assignment #4

Create function that adds elements to a list of
 unique elements, and returns True. If the element
 is not unique, it will not be added and returns
 False
"""

myUniqueList = []
myLeftoversList = []

def add_to_list(element):
    global myUniqueList
    if element in myUniqueList:
        add_to_leftovers(element)
        return False
    else:
        myUniqueList.append(element)
        return True


def add_to_leftovers(element):
    global myLeftoversList
    myLeftoversList.append(element)


def test_function(element):
    global myUniqueList, myLeftoversList
    if add_to_list(element):
        print("{} has been added to myUniqueList".format(element))
        print("The new list is:")
        print(myUniqueList)
        print()
    else:
        print("{} is already an element in myUniqueList".format(element))
        print("It will be added to myLeftoversList instead")
        print("That list now includes:")
        print(myLeftoversList)
        print()

test_function("Boxer")
test_function("Rebellion")
test_function(1903)
test_function("Whiskey")
test_function("Rebellion")
test_function(1789)
test_function("American")
test_function("Revolution")
test_function(1775)
test_function(["Apache", "Uprising", 1903])
test_function("Apache")
test_function("Uprising")
test_function(1903)
test_function(["Apache", "Uprising", 1903])
