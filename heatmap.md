``` python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example correlation matrix (10 columns, 8 rows)
data = np.random.uniform(-1, 1, (8, 10))  # Replace with your actual correlation data
correlation_matrix = pd.DataFrame(data, columns=[f'Col{i+1}' for i in range(10)])

# Define a custom color map
def custom_color_map(value):
    if -0.5 <= value < -0.3:
        return 'grey'  # Value between -0.5 and -0.3
    elif -0.3 <= value <= 0.3:
        return 'red'   # Value between -0.3 and 0.3
    elif 0.3 < value <= 1:
        return 'green' # Value between 0.3 and 1
    else:
        return 'white'  # Out of specified range

# Create a color array based on the custom color map
colors = np.array([[custom_color_map(val) for val in row] for row in correlation_matrix.values])

# Plotting the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", linewidths=.5, 
            cbar=False, cmap='gray', 
            linecolor='black', 
            mask=(correlation_matrix.isnull() | (correlation_matrix == 0)))

# Overlay custom colors
for i in range(correlation_matrix.shape[0]):
    for j in range(correlation_matrix.shape[1]):
        plt.gca().add_patch(plt.Rectangle((j, i), 1, 1, color=colors[i, j]))

plt.title('Custom Heatmap')
plt.xlabel('Columns')
plt.ylabel('Rows')
plt.show()
```
