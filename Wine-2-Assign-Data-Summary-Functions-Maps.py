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


# # Assigning data
# 
# Going the other way, assigning data to a DataFrame is easy. You can assign either a constant value:

# In[3]:


reviews


# In[4]:


reviews['critic'] = 'everyone'
reviews['critic']


# In[5]:


reviews.assign(critic_points=lambda x: x.points-5)


# Or with an iterable of values:

# In[6]:


reviews['index_backwards'] = range(len(reviews), 0, -1)
reviews['index_backwards']


# # Summary functions
# 
# Pandas provides many simple "summary functions" (not an official name) which restructure the data in some useful way. For example, consider the `describe()` method:

# In[7]:


reviews.points.describe()


# This method generates a high-level summary of the attributes of the given column. It is type-aware, meaning that its output changes based on the data type of the input. The output above only makes sense for numerical data; for string data here's what we get:

# In[8]:


reviews.taster_name.describe()


# If you want to get some particular simple summary statistic about a column in a DataFrame or a Series, there is usually a helpful pandas function that makes it happen. 
# 
# For example, to see the mean of the points allotted (e.g. how well an averagely rated wine does), we can use the `mean()` function:

# In[9]:


reviews.points.mean()


# In[10]:


reviews.points.median()


# To see a list of unique values we can use the `unique()` function:

# In[11]:


reviews.taster_name.unique()


# To see a list of unique values _and_ how often they occur in the dataset, we can use the `value_counts()` method:

# In[12]:


reviews.taster_name.value_counts()


# # Maps
# 
# A **map** is a term, borrowed from mathematics, for a function that takes one set of values and "maps" them to another set of values. In data science we often have a need for creating new representations from existing data, or for transforming data from the format it is in now to the format that we want it to be in later. Maps are what handle this work, making them extremely important for getting your work done!
# 
# There are two mapping methods that you will use often. 
# 
# [`map()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.map.html) is the first, and slightly simpler one. For example, suppose that we wanted to remean the scores the wines received to 0. We can do this as follows:

# In[13]:


review_points_mean = reviews.points.mean()
reviews.points.map(lambda p: p - review_points_mean)


# The function you pass to `map()` should expect a single value from the Series (a point value, in the above example), and return a transformed version of that value. `map()` returns a new Series where all the values have been transformed by your function.
# 
# [`apply()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.apply.html) is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row.

# In[14]:


def remean_points(row):
    row.points = row.points - review_points_mean
    return row

reviews.apply(remean_points, axis='columns')


# We'd like to host these wine reviews on our website, but a rating system ranging from 80 to 100 points is too hard to understand - we'd like to translate them into simple star ratings. A score of 95 or higher counts as 3 stars, a score of at least 85 but less than 95 is 2 stars. Any other score is 1 star.
# 
# Also, the Canadian Vintners Association bought a lot of ads on the site, so any wines from Canada should automatically get 3 stars, regardless of points.
# 
# Create a series `star_ratings` with the number of stars corresponding to each review in the dataset.

# In[15]:


def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')
star_ratings


# If we had called `reviews.apply()` with `axis='index'`, then instead of passing a function to transform each row, we would need to give a function to transform each *column*.
# 
# Note that `map()` and `apply()` return new, transformed Series and DataFrames, respectively. They don't modify the original data they're called on. If we look at the first row of `reviews`, we can see that it still has its original `points` value.

# In[16]:


reviews.head(1)


# Pandas provides many common mapping operations as built-ins. For example, here's a faster way of remeaning our points column:

# In[17]:


review_points_mean = reviews.points.mean()
reviews.points - review_points_mean


# In this code we are performing an operation between a lot of values on the left-hand side (everything in the Series) and a single value on the right-hand side (the mean value). Pandas looks at this expression and figures out that we must mean to subtract that mean value from every value in the dataset.
# 
# Pandas will also understand what to do if we perform these operations between Series of equal length. For example, an easy way of combining country and region information in the dataset would be to do the following:

# In[18]:


reviews.country + " - " + reviews.region_1


# I'm an economical wine buyer. Which wine is the "best bargain"? Create a variable `bargain_wine` with the title of the wine with the highest points-to-price ratio in the dataset.

# In[19]:


bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']
bargain_wine


# There are only so many words you can use when describing a bottle of wine. Is a wine more likely to be "tropical" or "fruity"? Create a Series `descriptor_counts` counting how many times each of these two words appears in the `description` column in the dataset. (For simplicity, let's ignore the capitalized versions of these words.)

# In[20]:


n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])
descriptor_counts

