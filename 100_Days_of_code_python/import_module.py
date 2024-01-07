# import math
# from math  import sqrt  as sq,pi,sin as s
# from math import * as x
# c = sq(0)
# print(dir(math))
# print("\n\n")
# print(dir(math.cos))

# script_a.py

from math import *

# Define a function called sin
def sin(x):
    return f"This is not the sin function from math, but a custom function: {x}"

# Using sin without the math prefix
result = sin(30)
print(result)
