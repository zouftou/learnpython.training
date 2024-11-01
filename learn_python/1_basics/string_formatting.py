"""
You will need to write a format string which prints out the data using the following syntax: Hello John Doe.
Your current balance is $53.44.
"""
if __name__ == '__main__':
    data = ("John", "Doe", 53.44)
    format_string = "Hello %s %s. Your current balance is $%s."

    print(format_string % data)