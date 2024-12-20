"""
In this exercise, you will need to add numbers and strings to the correct lists using the "append" list method. You must add
the numbers 1,2, and 3 to the "numbers" list, and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list, using the brackets operator [].
Note that the index is zero-based, so if you want to access the second item in the list, its index will be 1.
"""
if __name__ == '__main__':
    numbers = []
    strings = []
    names = ["John", "Eric", "Jessica"]

    # write your code here
    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    strings.append("hello")
    strings.append("world")

    second_name = names[1]

    # this code should write out the filled arrays and the second name in the names list (Eric).
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)