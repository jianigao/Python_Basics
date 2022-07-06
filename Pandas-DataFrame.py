#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})


# In[3]:


pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])


# In[4]:


# Create a DataFrame from a numpy array
my_data = np.random.randint(low=0, high=101, size=(6, 3))
my_column_names = ['c1', 'c2', 'c3']
df = pd.DataFrame(data=my_data, columns=my_column_names)

# use only specified columns
df[['c1', 'c2']]

# filter every nth row in a dataframe
df.iloc[::2, :][['c2', 'c3']]

# change column values
df['c1'] = df['c1'].map(lambda x: 'High' if float(x) > 50 else 'Low')
print(df)

# Get c1 and c3 value with highest c2 value
df.loc[df.c2.idxmax(), ['c1', 'c3']]


# In[5]:


df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))
# select a specific column (first column) from a dataframe as a dateframe
df[['a']]
df.loc[:, ['a']]
df.iloc[:, [0]]
# alternately the following returns a Series
df.a
df['a']
df.loc[:, 'a']
df.iloc[:, 0]

# select a specific row (first row) from a dataframe as a dateframe
df.loc[[0]]
df.loc[[0],:]
df.iloc[[0]]
df.iloc[[0],:]
# alternately the following returns a Series
df.loc[0]
df.loc[0,:]
df.iloc[0]
df.iloc[0,:]


# In[6]:


# change the order of columns of a dataframe
df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))

# In df , interchange columns 'a' and 'c' .
df[list('cbade')]

# Create a generic function to interchange two columns, without hardcoding column names.
def switch_columns(df, col1, col2):
    colnames = df.columns.tolist()
    i1, i2 = colnames.index(col1), colnames.index(col2)
    colnames[i2], colnames[i1] = colnames[i1], colnames[i2]
    return df[colnames]
df1 = switch_columns(df, 'a', 'c')

# Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.
df[sorted(df.columns)]
# or
df.sort_index(axis=1, ascending=False, inplace=True)


# In[7]:


# swap two rows of a dataframe
df = pd.DataFrame(np.arange(25).reshape(5, -1))
def swap_rows(df, i1, i2):
    a, b = df.iloc[i1, :].copy(), df.iloc[i2, :].copy()
    df.iloc[i1, :], df.iloc[i2, :] = b, a
    return df
swap_rows(df, 1, 2)


# In[8]:


# format or suppress scientific notations in a pandas dataframe
df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
# Solution 1: Rounding
df.round(4)
# Solution 2: Use apply to change format
df.apply(lambda x: '%.4f' % x, axis=1)
# or
df.applymap(lambda x: '%.4f' % x)
# Solution 3: Use set_option
pd.set_option('display.float_format', lambda x: '%.4f' % x)
# Solution 4: Assign display.float_format
pd.options.display.float_format = '{:.4f}'.format
# Reset/undo float formatting
pd.options.display.float_format = None


# In[9]:


# format all the values in a dataframe as percentages
df = pd.DataFrame(np.random.random(4), columns=['random'])
out = df.style.format({'random': '{0:.2%}'.format})
out


# In[10]:


# convert string percentages to numeric values
df = pd.DataFrame({'Percent': ['50%', '35%']})
print(df)
df['Percent'] = df['Percent'].str.strip('%')
df['Percent'] = pd.to_numeric(df['Percent'])
df


# In[11]:


# get the row number of the largest value in column 'a'
df = pd.DataFrame(np.random.randint(1, 10, 15).reshape(5,-1), columns=list('abc'))
print(df)
df['a'].argsort()[len(df['a'])-1]


# In[12]:


# get the last n rows of a dataframe with row sum > 100
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
# print row sums
rowsums = df.apply(np.sum, axis=1)
# last two rows with row sum greater than 100
last_two_rows = df.iloc[np.where([rowsums > 100])[1][-2:], :]
# or 
last_two_rows = df.iloc[np.where(rowsums > 100)[0][-2:], :]


# In[13]:


# create one-hot encodings of a categorical variable
df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))
df_onehot = pd.concat([pd.get_dummies(df['a']), df[list('bcde')]], axis=1)
df_onehot


# In[14]:


# find and cap outliers from a series or dataframe column
ser = pd.Series(np.linspace(-1, 1, 10))
def cap_outliers(ser, low_perc, high_perc):
    low, high = ser.quantile([low_perc, high_perc])
    print(low_perc, '%ile: ', low, '|', high_perc, '%ile: ', high)
    ser[ser < low] = low
    ser[ser > high] = high
    return(ser)
capped_ser = cap_outliers(ser, .05, .95)
capped_ser


# In[15]:


# reverse the rows of a dataframe
df = pd.DataFrame(np.arange(25).reshape(5, -1))
df.iloc[::-1, :]


# In[16]:


# remove rows from a dataframe that are present in another dataframe
df1 = pd.DataFrame({'fruit': ['apple', 'orange', 'banana'] * 3,
'weight': ['high', 'medium', 'low'] * 3,
'price': np.arange(9)})
df2 = pd.DataFrame({'fruit': ['apple', 'orange', 'pine'] * 2,
'weight': ['high', 'medium'] * 3,
'price': np.arange(6)})

print(df1[~df1.isin(df2).all(1)])


# In[17]:


# Return cumulative sum over a DataFrame or Series axis.
df = pd.DataFrame([[2.0, 1.0],
                   [3.0, np.nan],
                   [1.0, 0.0]],
                   columns=list('AB'))
# By default, iterates over rows and finds the sum in each column. 
# This is equivalent to axis=None or axis='index'.
df.cumsum()
# To iterate over columns and find the sum in each row, use axis=1.
df.cumsum(axis=1)


# In[18]:


# Percentage change between the current and a prior element.
# Shows computing the percentage change between rows.
df = pd.DataFrame({
    'FR': [4.0405, 4.0963, 4.3149],
    'GR': [1.7246, 1.7482, 1.8519],
    'IT': [804.74, 810.01, 860.13]},
    index=['1980-01-01', '1980-02-01', '1980-03-01'])
df.pct_change()
df.pct_change(periods=-1)
df.pct_change(fill_method='ffill')

# Shows computing the percentage change between columns.
df = pd.DataFrame({
    '2016': [176, 305],
    '2015': [150, 409],
    '2014': [137, 414]},
    index=['GOOG', 'APPL'])
df.pct_change(axis='columns')


# In[19]:


# Compute numerical data ranks (1 through n) along axis.
df = pd.DataFrame(data={'Animal': ['cat', 'penguin', 'dog',
                                   'spider', 'snake'],
                        'Number_legs': [4, 2, 4, 8, np.nan]})
df['default_rank'] = df['Number_legs'].rank()
df['max_rank'] = df['Number_legs'].rank(method='max')
df['NA_bottom'] = df['Number_legs'].rank(na_option='bottom')
df['pct_rank'] = df['Number_legs'].rank(pct=True)
df


# In[20]:


# Subset the dataframe rows or columns according to the specified index labels.
df = pd.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
                  index=['mouse', 'rabbit'],
                  columns=['one', 'two', 'three'])
# select columns by name
df.filter(items=['one', 'three'])
# select rows containing 'bbi'
df.filter(like='bbi', axis=0)


# In[21]:


# Iterate over (column name, Series) pairs.
df = pd.DataFrame({'species': ['bear', 'bear', 'marsupial'],
                  'population': [1864, 22000, 80000]},
                  index=['panda', 'polar', 'koala'])
print(df)
print()
for label, content in df.items():
    print(f'label: {label}')
    print(f'content: {content}', sep='\n')


# In[22]:


# Iterate over DataFrame rows as namedtuples.
df = pd.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
                  index=['dog', 'hawk'])
print(df)
print()
for row in df.itertuples(name='Animal'):
    print(row)


# In[23]:


# create a new column that contains the row number of nearest column by euclidean distance
df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
# init outputs
nearest_rows = []
nearest_distance = []
# iterate rows.
for i, row in df.iterrows():
    curr = row
    rest = df.drop(i)
    e_dists = {} # init dict to store euclidean dists for current row.
    # iterate rest of rows for current row
    for j, contestant in rest.iterrows():
        # compute euclidean dist and update e_dists
        e_dists.update({j: round(np.linalg.norm(curr.values - contestant.values))})
    # update nearest row to current row and the distance value
    nearest_rows.append(max(e_dists, key=e_dists.get))
    nearest_distance.append(max(e_dists.values()))
df['nearest_row'] = nearest_rows
df['dist'] = nearest_distance
df

