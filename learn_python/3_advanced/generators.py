import types

"""
Write a generator function which returns the Fibonacci series. They are calculated using the following formula:
The first two numbers of the series is always equal to 1, and each consecutive number returned is the sum of 
the last two numbers. Hint: Can you use only two variables in the generator function? Remember that assignments
can be done simultaneously.
"""
if __name__ == '__main__':
    # fill in this function
    def fib():
        a, b = 1, 1
        while 1:
            yield a
            a, b = b, a + b


    # testing code
    if type(fib()) == types.GeneratorType:
        print("Good, The fib function is a generator.")

        counter = 0
        for n in fib():
            print(n)
            counter += 1
            if counter == 10:
                break