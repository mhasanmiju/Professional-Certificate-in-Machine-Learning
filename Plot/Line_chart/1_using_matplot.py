# Plot/Line_chart/1_using_matplot.py
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line chart
plt.plot(x, y, label='sin(x)', color='blue')  # You can change color, style, etc.
plt.title('Line Chart using Matplotlib')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()