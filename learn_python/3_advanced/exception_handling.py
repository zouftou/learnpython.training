"""
Handle all the exception! Think back to the previous lessons to return the last name of the actor.
"""

def get_last_name():
    return actor["name"].split()[1]

if __name__ == '__main__':
    actor = {"name": "John Cleese", "rank": "awesome"}

    get_last_name()
    print("All exceptions caught! Good job!")
    print("The actor's last name is %s" % get_last_name())