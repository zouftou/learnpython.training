"""
Using a list comprehension, create a new list called "newlist" out of the list "numbers", which contains only the positive
numbers from the list, as integers.
"""
if __name__ == '__main__':
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = [int(x) for x in numbers if x > 0]
    print(newlist)