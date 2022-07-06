import numpy as np
import pandas as pd
pd.options.display.max_rows=5



# concat() Concatenate DataFrames or Series along a particular axis.

# Vertical (when columns are the same)
df = pd.concat([df1, df2])
df = pd.concat([df1, df2], axis=0)
# Horizontal (when indexes are the same)
df = pd.concat([df1, df2], axis=1)



# join() Join columns with other DataFrame either on index or on a key column.
# The lsuffix and rsuffix parameters are necessary when the datasets have
# the same column names.

# Join DataFrames using their indexes.
df1.join(df2, lsuffix='_1', rsuffix='_2')

# Join on a key column: we need to set key to be the index in both datasets. 
# The joined DataFrame will have key as its index.
df1.set_index("key").join(df2.set_index("key"))

# Another option to join using the key columns is to use the on parameter. 
# DataFrame.join always uses other’s index but we can use any column in df. 
# This method preserves the original DataFrame’s index in the result.
df.join(other.set_index('key'), on='key')

# Join on 2 key columns
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
left.join(right, lsuffix='_CAN', rsuffix='_UK')



# merge() Merge DataFrame or named Series objects with a database-style join.

# Merge df1 and df2 on the lkey and rkey columns. The value columns 
# have the default suffixes, _x and _y, appended.
df1.merge(df2, left_on='lkey', right_on='rkey')

# Merge DataFrames df1 and df2 with specified left and right suffixes 
# appended to any overlapping columns.
df1.merge(df2, left_on='lkey', right_on='rkey',
          suffixes=('_left', '_right'))
df1.merge(df2, left_on=['lkey1', 'lkey2'], right_on=['rkey1', 'rkey2'],
          suffixes=('_left', '_right'))

df1.merge(df2, how='inner', on='a')
df1.merge(df2, how='left', on='a')
df1.merge(df2, how='cross')

'''
how: {‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘inner’
Type of merge to be performed.

left: use only keys from left frame, similar to a SQL left outer join; preserve key order.
right: use only keys from right frame, similar to a SQL right outer join; preserve key order.
outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.
inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.
cross: creates the cartesian product from both frames, preserves the order of the left keys.
'''

# After merge, drop useless/redundant columns
df.drop(columns=['country','description'], inplace=True)
