import matplotlib.pyplot as plt
import numpy as np

#This will generate a random result
x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 