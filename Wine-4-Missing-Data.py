#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

np.set_printoptions(precision=2)
pd.options.display.float_format = '{:.2f}'.format
pd.options.display.max_rows = 6


# In[2]:


reviews = pd.read_csv("Datasets/winemag-data-130k-v2.csv", index_col=0)


# # Missing data
# 
# Entries missing values are given the value `NaN`, short for "Not a Number". For technical reasons these `NaN` values are always of the `float64` dtype.
# 
# Pandas provides some methods specific to missing data. To select `NaN` entries you can use `pd.isnull()` (or its companion `pd.notnull()`). This is meant to be used thusly:

# In[3]:


reviews


# In[4]:


# check if a dataframe has any missing values
reviews.isnull().values.any()


# In[5]:


# get the number of missing data points per column
missing_values_count = reviews.isnull().sum()
# or
missing_values_count = reviews.isna().sum()
missing_values_count


# In[6]:


# how many total missing values do we have?
total_cells = np.product(reviews.shape)
total_missing = missing_values_count.sum()
# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print("Percentage of missing data: %f" % percent_missing)


# In[7]:


reviews[pd.isnull(reviews.country)]


# Sometimes the price column is null. How many reviews in the dataset are missing a price?

# In[8]:


n_missing_prices = reviews.price.isnull().sum()
# or
n_missing_prices = pd.isnull(reviews.price).sum()
n_missing_prices


# In[9]:


# drop columns
reviews.drop(['points', 'price'], axis=1)
# or
reviews.drop(columns=['points', 'price'])
# drop rows by index
reviews.drop([0, 1])


# In[10]:


df = pd.DataFrame({
    'brand': ['Yum Yum', 'Yum Yum', 'Indomie', 'Indomie', 'Indomie'],
    'style': ['cup', 'cup', 'cup', 'pack', 'pack'],
    'rating': [4, 4, 3.5, 15, 5]
})
# remove duplicate rows based on all columns
df.drop_duplicates() 
# remove duplicates on specific column(s)
df.drop_duplicates(subset=['brand'])
# remove duplicates and keep last occurrences
df.drop_duplicates(subset=['brand', 'style'], keep='last')
# Return boolean Series denoting duplicate rows.
# By default, for each set of duplicated values, 
# the first occurrence is set on False and all others on True.
df.duplicated()
# By using ‘last’, the last occurrence of each set of duplicated 
# values is set on False and all others on True.
df.duplicated(keep='last')


# In[11]:


# Drop missing values
# remove all the rows that contain a missing value
df_row_dropped = reviews.dropna()
# remove all columns with at least one missing value
df_column_dropped = reviews.dropna(axis=1)
# 0, or ‘index’ : Drop rows which contain missing values.
# 1, or ‘columns’ : Drop columns which contain missing value.

# calculate number of dropped rows
rows_in_original_dataset = reviews.shape[0]
rows_in_na_dropped = df_row_dropped.shape[0]
dropped_rows = rows_in_original_dataset - rows_in_na_dropped

# just how much data did we lose?
print("Rows in original dataset: %d \n" % rows_in_original_dataset)
print("Rows with na's dropped: %d" % rows_in_na_dropped)


# Replacing missing values is a common operation.  Pandas provides a really handy method for this problem: `fillna()`. `fillna()` provides a few different strategies for mitigating such data. For example, we can simply replace each `NaN` with an `"Unknown"`:

# In[12]:


reviews.region_2.fillna("Unknown")
# fill in place
reviews['region_2'] = reviews['region_2'].fillna("Unknown")


# In[13]:


# Replace null-valued region_1 fields with the same value as for region_2
reviews['region_1'] = reviews['region_1'].fillna(reviews['region_2'])
reviews


# In[14]:


# replace NA prince with 0
reviews.price.fillna(0)


# In[15]:


# replace missing values with the mean
reviews.price.fillna(reviews.price.mean())


# Or we could fill each missing value with the first non-null value that appears sometime after the given record in the database. This is known as the backfill strategy.

# In[16]:


# fill with next value else previous value
reviews.price.fillna(method='bfill', axis=0).fillna(method='ffill', axis=0)


# In[17]:


reviews.price.ffill() # fill with previous value
reviews.price.bfill() # fill with next value
reviews.price.bfill().ffill() # fill with next value else with previous value


# What are the most common wine-producing regions? Create a Series counting the number of times each value occurs in the `region_1` field. This field is often missing data, so replace missing values with `Unknown`. Sort in descending order.

# In[18]:


reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
reviews_per_region


# Alternatively, we may have a non-null value that we would like to replace. For example, suppose that since this dataset was published, reviewer Kerin O'Keefe has changed her Twitter handle from `@kerinokeefe` to `@kerino`. One way to reflect this in the dataset is using the `replace()` method:

# In[19]:


reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino")


# The `replace()` method is worth mentioning here because it's handy for replacing missing data which is given some kind of sentinel value in the dataset: things like `"Unknown"`, `"Undisclosed"`, `"Invalid"`, and so on.
