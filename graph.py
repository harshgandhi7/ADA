import numpy as np
import matplotlib.pyplot as plt
# Specify the file path
file_path = 'data.txt'

# Read data into two arrays using numpy
data = np.loadtxt(file_path, delimiter=',', skiprows=0)  # Assuming CSV with a header row

# Separate the data into two arrays
x = data[:, 0]
y = data[:, 1]

# Print the arrays
print("X values:", x)
print("Y values:", y)

# Create a plot with customizations
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='Line 1')

# Add labels and a title
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Customized Plot')

# Add a grid
plt.grid(True)

# Add a legend
plt.legend()

# Show the plot
plt.show()
 