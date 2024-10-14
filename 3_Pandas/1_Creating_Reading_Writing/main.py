import pandas as pd


# There are two core objects in pandas: the DataFrame and the Series.

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})



movie_data = pd.DataFrame({'Bob': ['I like it.', 'It was awful.'],
              'Sue': ['Pretty good', 'bland.']},
             index=['Product A', 'Product B'])

# save data into anthor file 
# DataFrame.to_csv(filename, sep=',', index=False, encoding='utf-8')

movie_data.to_csv('movie_data.csv', sep=',', index=True, encoding='utf-8')


pd.Series([1, 2, 3, 4, 5])



# Series do have name => only has one name for all series
# Series a single column of a DataFrame

pd.Series([43, 32, 21], index=['2020 Sale', '2021 Sales', '2022 Sales'], name='Product A')


