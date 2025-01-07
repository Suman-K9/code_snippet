```python
import pandas as pd

# Sample DataFrames
data1 = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [2, 3, 4, 5, 6]
}

data2 = {
    'D': [2, 3, 4, 5, 6],
    'E': [5, 6, 7, 8, 9]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Initialize a dictionary to store the correlation results
correlation_results = {}

# Calculate correlation for each column in df1 against each column in df2
for col1 in df1.columns:
    for col2 in df2.columns:
        correlation = df1[col1].corr(df2[col2])
        correlation_results[(col1, col2)] = correlation

# Convert the results to a DataFrame for better visualization
correlation_df = pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Correlation'])
correlation_df.index = pd.MultiIndex.from_tuples(correlation_df.index, names=['DataFrame1', 'DataFrame2'])

# Display the correlation DataFrame
print(correlation_df)
```
