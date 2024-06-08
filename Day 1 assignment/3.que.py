'''
Python program that calculates the square root of a non-negative number entered by the user,
handles exceptions such as ValueError and NameError,
includes an else block to print the square root if no exception occurs,
and a finally block to ensure that the program execution is completed:
'''

import math

try:
    num = float(input("Enter a non-negative number: "))
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
    sqrt = math.sqrt(num)
except ValueError as e:
    print(f"Error: {e}")
except NameError as e:
    print(f"Error: {e}")
else:
    print(f"The square root of {num} is {sqrt}")
finally:
    print("Program execution completed.")