import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])

x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

x3 = np.array([0, 11, 12, 13])
y3 = np.array([6, 12, 7, 11])


def multiple_line():
    # Draw two lines by specifiyng the x- and y-point values for both lines:
    plt.plot(x1, y1,  x2, y2,  x3, y3)
    plt.show()

def subplot():
    # `plt.figure(figsize=(width, height))` function use Before creating the subplots. For example,
    # `plt.figure(figsize=(10, 5))` will create a figure with a width of 10 inches and a height of 5
    # inches.
    plt.figure(figsize=(12, 5))
    
    #subplot() function use to draw multiple plots in ONE figure:
    # rows and columns, index of the current plot.
    plt.subplot(1, 3, 1)
    plt.plot(x1,y1,"orange")
    plt.title("First")  #order matters *********

    plt.subplot(1, 3, 2)
    plt.plot(x2,y2)
    plt.title("Second") #order matters *********
    
    plt.subplot(1, 3, 3)
    plt.plot(x3,y3,"g")
    plt.title("Third")  #order matters *********

    #Title to the entire figure with the suptitle() function:
    plt.suptitle("Supertitle")
    plt.show()

# multiple_line()
subplot()