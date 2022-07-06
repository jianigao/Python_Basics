import numpy as np
import pandas as pd


# Scaling
from sklearn.preprocessing import MinMaxScaler
X = MinMaxScaler().fit_transform(X)
# or
X = (X - X.min())/(X.max() - X.min())

# Normalization
from sklearn.preprocessing import StandardScaler
X = StandardScaler().fit_transform(X)
# or
X = (X - X.mean())/X.std()