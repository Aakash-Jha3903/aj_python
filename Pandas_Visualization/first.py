import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {'x': range(10), 'y': [i**2 for i in range(10)]}
df = pd.DataFrame(data)

# Plot a line graph
df.plot(x='x', y='y', kind='line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()
