from functools import partial

"""
Edit the function provided by calling partial() and replacing the first three variables in func().
Then print with the new partial function using only one input variable so that the output equals 60.
"""

def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x

if __name__ == '__main__':
    p = partial(func, 5, 6, 7)
    print(p(8))