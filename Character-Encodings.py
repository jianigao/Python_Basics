# modules we'll use
import pandas as pd
import numpy as np

# helpful character encoding module
import chardet

# set seed for reproducibility
np.random.seed(0)


sample_entry = b'\xa7A\xa6n'
print(sample_entry)
print('data type:', type(sample_entry))
# bytes

# decode
before = sample_entry.decode("big5-tw")

# encode it to a different encoding, replacing characters that raise errors
new_entry = before.encode("utf-8", errors="replace")

# save to CSV
new_entry.to_csv("my_file.csv")
    

# look at the first ten thousand bytes to guess the character encoding
with open("../PoliceKillingsUS.csv", 'rb') as rawdata:
    result = chardet.detect(rawdata.read(100000))
# {'encoding': 'Windows-1252', 'confidence': 0.73, 'language': ''}

police_killings = pd.read_csv("../PoliceKillingsUS.csv", encoding='Windows-1252')