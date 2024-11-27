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
plt.show()
