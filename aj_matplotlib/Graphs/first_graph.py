# % matplotlib inline     #for jupiter
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

x = [1, 15, 13, 42, 15]   # len of x and y must be same !!
y = [i for i in range(0, 10, 2)]
# plt.plot([1, 2, 3, 4], [1, 10, 19, 16])  #we plot without using separate variables

plt.plot(x, y, color="orangered", linewidth=2, linestyle="dotted")

# plt.plot(x, y, marker="+" , markersize="20")    # marker is used for point custmization(color,pattern,size,etc)

# plt.plot(x, y,"o:r")     # marker|line|color  , without space

# plt.plot(x,y,alpha=0.5)     # alpha is from 0 to 1 , it defines the visibility level of line

font1 = {'family': 'serif', 'color': 'red', 'size': 20}
font2 = {'family': 'serif', 'color':"b", 'size': 15}

plt.title("Student Data", fontdict=font1 ,  loc = 'left')
plt.xlabel("student", fontdict=font2)
plt.ylabel("Class", fontdict=font2)

plt.grid()  # add grid in the background

# plt.scatter(x, y)     # directly map the points only

plt.show()  # To display the plot
