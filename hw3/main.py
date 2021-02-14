"""
pirple/python/hw3/main.py
Homework Assignment #3

Create function that determines if 2 or more of the passed
 parameter values are equal (including strings with numbers
 as their value)
"""

def two_are_equal(a, b, c):
    if int(a) == int(b):
        result = True
    elif int(a) == int(c):
        result = True
    elif int(b) == int(c):
        result = True
    else:
        result = False

    return result

def check_equality(a, b, c):
    if two_are_equal(a, b, c):
        print("At least 2 of these numbers ({},{},{}) are equal".format(a,b,c))
    else:
        print("None of these numbers ({},{},{}) are equal".format(a,b,c))

check_equality(1, 2, 3)
check_equality(3, 2, 3)
check_equality(1, 1, 1)
check_equality(1, 2, 1)
check_equality(1, 2, "2")
check_equality("1", "2", "2")
check_equality("1", "2", "3")
