"""
In the exercise below, use the given lists to print out a set containing all the participants from event A which did not attend event B.
"""
if __name__ == '__main__':
    a = ["Jake", "John", "Eric"]
    b = ["John", "Jill"]

    A = set(a)
    B = set(b)

    print(A.difference(B))