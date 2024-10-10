```python

words_to_search = ['word1', 'word2', 'word3']

import re
pattern = '|'.join(words_to_search)

import pandas as pd

# assume df is your dataframe
df = pd.DataFrame({
    'column1': ['hello world1', 'foo bar', 'baz qux'],
    'column2': ['qux word2', 'corge grault', 'garply word3']
})

# search for the pattern in each column
mask = df.apply(lambda x: x.str.contains(pattern, case=False, na=False))

# use the mask to filter the dataframe
result_df = df[mask.any(axis=1)]
import pandas as pd
import re

def search_words_in_df(df, words_to_search):
    pattern = '|'.join(words_to_search)
    mask = df.apply(lambda x: x.str.contains(pattern, case=False, na=False))
    return df[mask.any(axis=1)]

# example usage
words_to_search = ['word1', 'word2', 'word3']
df = pd.DataFrame({
    'column1': ['hello world1', 'foo bar', 'baz qux'],
    'column2': ['qux word2', 'corge grault', 'garply word3']
})

result_df = search_words_in_df(df, words_to_search)
print(result_df)

```