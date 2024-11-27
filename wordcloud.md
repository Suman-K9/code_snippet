``` python
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Step 1: Load data into a pandas DataFrame
data = {
    'text': [
        'Python is great for data analysis.',
        'Data science is an exciting field.',
        'Machine learning is a subset of artificial intelligence.',
        'Pandas is a powerful library for data manipulation.',
        'Word clouds are a fun way to visualize text data.'
    ]
}
df = pd.DataFrame(data)

# Step 2: Combine all text into a single string
text = ' '.join(df['text'])

# Step 3: Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Step 4: Display the word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Turn off axis numbers and ticks

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Step 1: Load data from an Excel file into a pandas DataFrame
# Replace 'your_file.xlsx' with the path to your Excel file
df = pd.read_excel('your_file.xlsx', engine='openpyxl')

# Step 2: Loop through each column and create a word cloud
for column in df.columns:
    # Combine all text from the current column into a single string
    text = ' '.join(df[column].dropna().astype(str))  # Convert to string and drop NaN values

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Display the word cloud using matplotlib
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Turn off axis numbers and ticks
    plt.title(f'Word Cloud for {column}')
    plt.show()
```
plt.show()
