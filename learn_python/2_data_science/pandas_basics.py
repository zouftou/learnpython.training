import pandas as pd

"""
There are several ways to create a DataFrame.
One way way is to use a dictionary.
"""
if __name__ == '__main__':
    dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
            "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
            "area": [8.516, 17.10, 3.286, 9.597, 1.221],
            "population": [200.4, 143.5, 1252, 1357, 52.98]}

    brics = pd.DataFrame(dict)
    print(brics)