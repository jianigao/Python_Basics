#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


# create a TimeSeries starting ‘2000-01-01’ and 10 weekends 
# (saturdays) after that having random numbers as values
pd.Series(np.random.randint(1,10,10), pd.date_range('2022-06-03', periods=10, freq='W-SAT'))


# In[3]:


# convert year-month string to dates corresponding to the 4th day of the month
ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])
# Solution
from dateutil.parser import parse
ser.map(lambda x: parse('04'+x))


# In[4]:


# get the day of month, week number, day of year and day of week from a series of date strings
ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])
# convert a series of date-strings to a timeseries
ser_ts = pd.to_datetime(ser)
# day of month
print("Date: ", ser_ts.dt.day.tolist())
# week number
print("Week number: ", ser_ts.dt.isocalendar().week.tolist())
# day of year
print("Day number of year: ", ser_ts.dt.dayofyear.tolist())
# day of week
print("Day of week: ", ser_ts.dt.day_name().tolist())


# In[5]:


# create lags and leads of a column in a dataframe
df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))
# Solution
df['a_lag1'] = df['a'].shift(1)
df['b_lead1'] = df['b'].shift(-1)
print(df)

