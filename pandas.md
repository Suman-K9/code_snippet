```python
import pandas as pd
import streamlit as st

# Sample DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D'],
    'Percentage': [45, 76, 90, 30]
}
df = pd.DataFrame(data)

# Function to apply colors
def color_percentage(val):
    """Apply color based on percentage value."""
    if val >= 75:
        color = 'green'
    elif val >= 50:
        color = 'orange'
    else:
        color = 'red'
    return f'background-color: {color}; color: white;'

# Style the DataFrame
styled_df = df.style.applymap(color_percentage, subset=['Percentage'])

# Streamlit App
st.title("Percentage Column with Conditional Coloring")

st.write("Below is the DataFrame with the percentage column styled:")

# Display styled DataFrame
st.dataframe(styled_df)


import pandas as pd
import streamlit as st

# Sample DataFrame
data = {
    'Name': ['A', 'B', 'C', 'D', 'E'],
    'Percentage': [45, 76, 90, 30, 65]
}
df = pd.DataFrame(data)

# Apply Heatmap Style using pandas
styled_df = df.style.background_gradient(cmap='YlOrRd', subset=['Percentage'])

# Streamlit App
st.title("Percentage Column Heatmap")

st.write("The 'Percentage' column is displayed as a heatmap based on its values:")

# Display styled DataFrame
st.dataframe(styled_df)

```