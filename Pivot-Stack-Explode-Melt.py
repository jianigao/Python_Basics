#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})
df


# In[3]:


# pivot_table has an aggregation function
table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum, fill_value=0)
table


# In[4]:


table = pd.pivot_table(df, values=['D', 'E'], index=['A', 'C'],
                    aggfunc={'D': np.mean,
                             'E': [min, max, np.mean]})
table


# In[5]:


# Pivot without aggregation that can handle non-numeric data
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df


# In[6]:


df.pivot(index='foo', columns='bar', values='baz')


# In[7]:


df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])


# In[8]:


df = pd.DataFrame({
       "lev1": [1, 1, 1, 2, 2, 2],
       "lev2": [1, 1, 2, 1, 1, 2],
       "lev3": [1, 2, 1, 2, 1, 2],
       "lev4": [1, 2, 3, 4, 5, 6],
       "values": [0, 1, 2, 3, 4, 5]})
df


# In[9]:


df.pivot(index="lev1", columns=["lev2", "lev3"],values="values")


# In[10]:


df.pivot(index=["lev1", "lev2"], columns=["lev3"],values="values")


# In[11]:


# Stack the prescribed level(s) from columns to index
df_single_level_cols = pd.DataFrame([[0, 1], [2, 3]],
                                    index=['cat', 'dog'],
                                    columns=['weight', 'height'])
df_single_level_cols


# In[12]:


df_single_level_cols.stack()


# In[13]:


multicol1 = pd.MultiIndex.from_tuples([('weight', 'kg'),
                                       ('weight', 'pounds')])
df_multi_level_cols1 = pd.DataFrame([[1, 2], [2, 4]],
                                    index=['cat', 'dog'],
                                    columns=multicol1)
df_multi_level_cols1


# In[14]:


df_multi_level_cols1.stack()


# In[15]:


multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
                                       ('height', 'm')])
df_multi_level_cols2 = pd.DataFrame([[1.0, 2.0], [3.0, 4.0]],
                                    index=['cat', 'dog'],
                                    columns=multicol2)
df_multi_level_cols2


# In[16]:


df_multi_level_cols2.stack()


# In[17]:


df_multi_level_cols2.stack(0)


# In[18]:


df_multi_level_cols2.stack([0, 1])


# In[19]:


# Pivot a level of the (necessarily hierarchical) index labels
index = pd.MultiIndex.from_tuples([('one', 'a'), ('one', 'b'),
                                   ('two', 'a'), ('two', 'b')])
s = pd.Series(np.arange(1.0, 5.0), index=index)
s


# In[20]:


s.unstack(level=-1)


# In[21]:


s.unstack(level=0)


# In[22]:


s.unstack(level=0).unstack()


# In[23]:


# Transform each element of a list-like to a row, replicating index values
df = pd.DataFrame({'A': [[0, 1, 2], 'foo', [], [3, 4]],
                   'B': 1,
                   'C': [['a', 'b', 'c'], np.nan, [], ['d', 'e']]})
df


# In[24]:


df.explode('A')


# In[25]:


df.explode(list('AC'))
# or 
df.explode(['A','C'])


# In[26]:


# Unpivot a DataFrame from wide to long format, optionally leaving identifiers set
df = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})
df


# In[27]:


df.melt(id_vars=['A'], value_vars=['B'])


# In[28]:


df.melt(id_vars=['A'], value_vars=['B', 'C'])

