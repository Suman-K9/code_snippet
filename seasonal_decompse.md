``` python
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

# Load the time series data
ts = pd.read_csv('data.csv', index_col='date', parse_dates=['date'])

# Perform additive decomposition
result_add = seasonal_decompose(ts, model='additive')

# Plot the trend component
plt.figure(figsize=(9, 3))
plt.plot(result_add.trend, label='Additive Trend')
plt.legend()

# Plot the seasonal component
plt.figure(figsize=(9, 3))
plt.plot(result_add.seasonal, label='Additive Seasonal')
plt.legend()
```
