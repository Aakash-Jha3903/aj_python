import matplotlib.pyplot as plt 

def axis_range():
    x = [1, 15, 13, 42, 15]   # len of x and y must be same !!
    y = [i for i in range(0, 10, 2)]

    plt.plot(x,y)
    plt.axis([0, 600, 0, 200])  # axis range [xmin, xmax, ymin, ymax]
    plt.show()

def figure_size():
    from matplotlib.figure import Figure  

    # Creating a new figure with width = 5 inches and height = 4 inches 
    fig = plt.figure(figsize =(5, 4)) 
    
    # Creating a new axes for the figure 
    ax = fig.add_axes([1, 1, 1, 1])  

    # Adding the data to be plotted 
    ax.plot([2, 3, 4, 5, 5, 6, 6], [5, 7, 1, 3, 4, 6 ,8]) 

    plt.show()


axis_range()
figure_size()