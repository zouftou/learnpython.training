import numpy as np

"""
First, convert the list of weights from a list to a Numpy array. Then, convert all of the weights from kilograms to pounds.
Use the scalar conversion of 2.2 lbs per kilogram to make your conversion. Lastly, print the resulting array of weights in pounds.
"""
if __name__ == '__main__':
    weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    # Create a numpy array np_weight_kg from weight_kg
    np_weight_kg = np.array(weight_kg)

    # Create np_weight_lbs from np_weight_kg
    np_weight_lbs = np_weight_kg * 2.2

    # Print out np_weight_lbs
    print(np_weight_lbs)