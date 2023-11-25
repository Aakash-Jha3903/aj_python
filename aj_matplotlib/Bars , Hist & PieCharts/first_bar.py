import matplotlib.pyplot as plt
import numpy as np

x = ["A", "B", "C", "D"]
y = [4, 9, 5, 11]

plt.bar(x,y ,color = "hotpink" ,width = 0.1)
plt.show()
# plt.barh(x, y)  # h for horizontal
plt.show()

def barh():
    plt.bar(x,y ,color = "hotpink" ,height = 0.1)   # For horizontal bars, use height instead of width.
    plt.show()