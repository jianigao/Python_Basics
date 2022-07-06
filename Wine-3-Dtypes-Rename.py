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


# # Dtypes
# 
# The data type for a column in a DataFrame or a Series is known as the **dtype**.
# 
# You can use the `dtype` property to grab the type of a specific column.  For instance, we can get the dtype of the `price` column in the `reviews` DataFrame:

# In[3]:


reviews.price.dtype


# Alternatively, the `dtypes` property returns the `dtype` of _every_ column in the DataFrame:

# In[4]:


reviews.dtypes


# In[5]:


# how many columns under each dtype
reviews.dtypes.value_counts()


# Data types tell us something about how pandas is storing the data internally. `float64` means that it's using a 64-bit floating point number; `int64` means a similarly sized integer instead, and so on.
# 
# One peculiarity to keep in mind (and on display very clearly here) is that columns consisting entirely of strings do not get their own type; they are instead given the `object` type.
# 
# It's possible to convert a column of one type into another wherever such a conversion makes sense by using the `astype()` function. For example, we may transform the `points` column from its existing `int64` data type into a `float64` data type:

# In[6]:


reviews.points.astype('float64')


# Create a Series from entries in the `points` column, but convert the entries to strings. Hint: strings are `str` in native Python.

# In[7]:


reviews.points.astype('str')


# In[8]:


# convert to a numeric type
reviews['points'] = pd.to_numeric(reviews['points'])


# A DataFrame or Series index has its own `dtype`, too:

# In[9]:


reviews.index.dtype


# Pandas also supports more exotic data types, such as categorical data and timeseries data. Because these data types are more rarely used, we will omit them until a much later section of this tutorial.

# # Renaming
# 
# The first function we'll introduce here is `rename()`, which lets you change index names and/or column names. For example, to change the `points` column in our dataset to `score`, we would do:

# In[10]:


reviews.rename(columns={'points': 'score'})


# `region_1` and `region_2` are pretty uninformative names for locale columns in the dataset. Create a copy of `reviews` with these columns renamed to `region` and `locale`, respectively.

# In[11]:


reviews.rename(columns={'region_1': 'region','region_2' : 'locale'})


# `rename()` lets you rename index _or_ column values by specifying a `index` or `column` keyword parameter, respectively. It supports a variety of input formats, but usually a Python dictionary is the most convenient. Here is an example using it to rename some elements of the index.

# In[12]:


reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'})


# You'll probably rename columns very often, but rename index values very rarely.  For that, `set_index()` is usually more convenient.
# 
# Both the row index and the column index can have their own `name` attribute. The complimentary `rename_axis()` method may be used to change these names. For example:

# In[13]:


reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns')

