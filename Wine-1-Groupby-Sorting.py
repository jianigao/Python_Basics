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


# # Groupwise analysis
# 
# One function we've been using heavily thus far is the `value_counts()` function. We can replicate what `value_counts()` does by doing the following:

# In[3]:


reviews.points.value_counts().sort_index()


# In[4]:


reviews.groupby('points').points.count()


# In[5]:


reviews.groupby('points').size()


# `groupby()` created a group of reviews which allotted the same point values to the given wines. Then, for each of these groups, we grabbed the `points()` column and counted how many times it appeared.  `value_counts()` is just a shortcut to this `groupby()` operation. 
# 
# We can use any of the summary functions we've used before with this data. For example, to get the cheapest wine in each point value category, we can do the following:

# In[6]:


reviews.groupby('points').price.min()


# In[7]:


# keep the grouped column as another column (not index)
reviews.groupby('points', as_index=False)['price'].min()


# In[8]:


# get the particular group of a groupby dataframe by key
reviews.groupby('points').get_group(99)


# In[9]:


# get the n’th largest value of a column when grouped by another column
reviews['price'].groupby(reviews.points).get_group(99).sort_values(ascending=False).iloc[2]


# Create a `Series` whose index is reviewers and whose values is the average review score given out by that reviewer. Hint: you will need the `taster_name` and `points` columns.

# In[10]:


reviewer_mean_ratings = reviews.groupby('taster_name').points.mean()
reviewer_mean_ratings


# Are there significant differences in the average scores assigned by the various reviewers? Run the cell below to use the `describe()` method to see a summary of the range of values.

# In[11]:


reviewer_mean_ratings.describe()


# Who are the most common wine reviewers in the dataset? Create a `Series` whose index is the `taster_twitter_handle` category from the dataset, and whose values count how many reviews each person wrote.

# In[12]:


reviews.groupby('taster_twitter_handle').size()


# You can think of each group we generate as being a slice of our DataFrame containing only data with values that match. This DataFrame is accessible to us directly using the `apply()` method, and we can then manipulate the data in any way we see fit. For example, here's one way of selecting the name of the first wine reviewed from each winery in the dataset:

# In[13]:


reviews.groupby('winery').apply(lambda df: df.title.iloc[0])


# For even more fine-grained control, you can also group by more than one column. For an example, here's how we would pick out the best wine by country _and_ province:

# In[14]:


reviews.groupby(['country', 'province']).apply(lambda df: df.loc[df.points.idxmax()])


# Another `groupby()` method worth mentioning is `agg()`, which lets you run a bunch of different functions on your DataFrame simultaneously. For example, we can generate a simple statistical summary of the dataset as follows:

# In[15]:


ds = reviews.groupby('country').price.agg([len, min, max])
ds


# In[16]:


ds['min'].sort_values()


# Effective use of `groupby()` will allow you to do lots of really powerful things with your dataset.

# In[17]:


# Call func on self producing a DataFrame with the same axis shape as self.
reviews.groupby('country')['price'].transform('mean')


# # Multi-indexes
# 
# In all of the examples we've seen thus far we've been working with DataFrame or Series objects with a single-label index. `groupby()` is slightly different in the fact that, depending on the operation we run, it will sometimes result in what is called a multi-index.
# 
# A multi-index differs from a regular index in that it has multiple levels. For example:

# In[18]:


countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
countries_reviewed


# In[19]:


mi = countries_reviewed.index
type(mi)


# Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. They also require two levels of labels to retrieve a value. Dealing with multi-index output is a common "gotcha" for users new to pandas.
# 
# The use cases for a multi-index are detailed alongside instructions on using them in the [MultiIndex / Advanced Selection](https://pandas.pydata.org/pandas-docs/stable/advanced.html) section of the pandas documentation.
# 
# However, in general the multi-index method you will use most often is the one for converting back to a regular index, the `reset_index()` method:

# In[20]:


countries_reviewed.reset_index()


# # Sorting
# 
# Looking again at `countries_reviewed` we can see that grouping returns data in index order, not in value order. That is to say, when outputting the result of a `groupby`, the order of the rows is dependent on the values in the index, not in the data.
# 
# To get data in the order want it in we can sort it ourselves.  The `sort_values()` method is handy for this.

# In[21]:


countries_reviewed = countries_reviewed.reset_index()
countries_reviewed.sort_values(by='len')


# `sort_values()` defaults to an ascending sort, where the lowest values go first. However, most of the time we want a descending sort, where the higher numbers go first. That goes thusly:

# In[22]:


countries_reviewed.sort_values(by='len', ascending=False)


# To sort by index values, use the companion method `sort_index()`. This method has the same arguments and default order:

# In[23]:


countries_reviewed.sort_index()


# Finally, know that you can sort by more than one column at a time:

# In[24]:


countries_reviewed.sort_values(by=['country', 'len'])


# What is the best wine I can buy for a given amount of money? Create a `Series` whose index is wine prices and whose values is the maximum number of points a wine costing that much was given in a review. Sort the values by price, ascending (so that `4.0` dollars is at the top and `3300.0` dollars is at the bottom).

# In[25]:


best_rating_per_price = reviews.groupby('price')['points'].max().sort_index()
best_rating_per_price


# What are the minimum and maximum prices for each `variety` of wine? Create a `DataFrame` whose index is the `variety` category from the dataset and whose values are the `min` and `max` values thereof.

# In[26]:


price_extremes = reviews.groupby('variety').price.agg([min, max])
price_extremes


# What are the most expensive wine varieties? Create a variable `sorted_varieties` containing a copy of the dataframe from the previous question where varieties are sorted in descending order based on minimum price, then on maximum price (to break ties).

# In[27]:


sorted_varieties = price_extremes.sort_values(by=['min', 'max'], ascending=False)
sorted_varieties


# What combination of countries and varieties are most common? Create a `Series` whose index is a `MultiIndex`of `{country, variety}` pairs. For example, a pinot noir produced in the US should map to `{"US", "Pinot Noir"}`. Sort the values in the `Series` in descending order based on wine count.

# In[28]:


country_variety_counts = reviews.groupby(['country', 'variety']).size().sort_values(ascending=False)
country_variety_counts

