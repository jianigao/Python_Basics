#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
#print(pd.__version__)
#print(pd.show_versions(as_json=True))


# In[2]:


ser = pd.Series([1, 2, 3, 4, 5])
ser


# In[3]:


ser = pd.Series([30, 35, 40],
              index=['2015 Sales', '2016 Sales', '2017 Sales'],
              name='Product A')
ser


# In[4]:


# convert the index of a series into a column of a dataframe
df = ser.to_frame().reset_index()
df


# In[5]:


# assign name to the series’ index
ser = pd.Series(list('abced'))
ser.name = 'alphabets'
ser


# In[6]:


# extract items at given positions from a series
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
ser.take(pos)


# In[7]:


# create a series from a list, numpy array and dict
mylist = list('abced')
myarr = np.arange(5)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
ser


# In[8]:


# convert a numpy array to a dataframe of given shape
ser = pd.Series(np.random.randint(1, 10, 24))
df = pd.DataFrame(ser.values.reshape(4,6))
df


# In[9]:


# combine many series to form a dataframe
ser1 = pd.Series(list('abced'))
ser2 = pd.Series(np.arange(5))
# Solution 1
df = pd.concat([ser1, ser2], axis=1)
# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
df


# In[10]:


# get the items of series A not present in series B
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1[~ser1.isin(ser2)]


# In[11]:


# get the items not common to both series A and series B
ser_u = pd.Series(np.union1d(ser1, ser2)) # union
ser_i = pd.Series(np.intersect1d(ser1, ser2)) # intersect
ser_u[~ser_u.isin(ser_i)]


# In[12]:


# get the positions of items of series A in another series B
ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])
[pd.Index(ser1).get_loc(i) for i in ser2]


# In[13]:


# keep only top 2 most frequent values as it is and replace everything else as ‘Other’
ser = pd.Series(np.random.randint(1, 5, [6]))
print("Freqency:\n", ser.value_counts())
ser[~ser.isin(ser.value_counts().index[:2])] = 'Other'
ser


# In[14]:


# get the min, 25th, median, 75th, and max of a numeric series
ser = pd.Series(np.arange(26))
np.percentile(ser, q=[0, 25, 50, 75, 100])


# In[15]:


# bin a numeric series to 10 groups of equal size
ser = pd.Series(np.random.rand(20))
print(ser.head())
pd.qcut(ser, q=[0, .10, .20, .3, .4, .5, .6, .7, .8, .9, 1],
labels=['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']).head()


# In[16]:


# compute difference of differences between consequtive numbers of a series
ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])
print(ser.diff().tolist())
print(ser.diff().diff().tolist())


# In[17]:


# replace missing spaces in a string with the least frequent character
ser = pd.Series(list('dbc deb abed gade'))
freq = ser.value_counts()
least_freq = freq.dropna().index[-1]
"".join(ser.replace(' ', least_freq))


# In[18]:


# filter words that contain at least 2 vowels from a series
ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])
result = ser[ser.str.count('[AEIOUaeiou]') >=2]
result


# In[19]:


# filter valid emails from a series
emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
import re
pattern ='[A-Za-z0-9.-_]+@[A-Za-z0-9.-]+.[A-Za-z]{2,4}'
mask = emails.map(lambda x: bool(re.match(pattern, x)))
emails[mask].to_list()

