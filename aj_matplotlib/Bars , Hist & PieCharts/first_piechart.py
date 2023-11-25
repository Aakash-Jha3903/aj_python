import matplotlib.pyplot as plt
import numpy as np

mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0.5, 0, 1]
mycolors = ["black", "hotpink", "g", "r"]

x = [35, 25, 25, 15]

# default start angle is at the x-axis, but you can change the start angle by specifying a startangle paramete(default angle is 0).
# plt.pie(x, labels = mylabels, startangle = 90)

# plt.pie(x, labels=mylabels, explode=myexplode, shadow=True,colors=mycolors)

plt.pie(x, labels=mylabels)
plt.legend()    # To add a list of explanation for each wedge, use the legend() function:
plt.title("Fruits Pie-Charts")
plt.show()
