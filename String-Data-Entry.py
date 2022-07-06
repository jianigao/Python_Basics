import pandas as pd
import numpy as np


ser = pd.Series(['how', 'to', 'do', 'it?'])
# convert the first character of each element in a series to uppercase
ser.str.title()
# calculate the number of characters in each word in a series
ser.str.len()


# convert to lower case
df['Country'] = df['Country'].str.lower()
# remove leading and trailing white spaces
df['Country'] = df['Country'].str.strip()
# remove leading white spaces
df['Country'] = df['Country'].str.lstrip()
# remove trailing white spaces
df['Country'] = df['Country'].str.rstrip()


# split a text column into two separate columns
df = pd.DataFrame(["STD, City State",
"33, Kolkata West Bengal",
"44, Chennai Tamil Nadu",
"40, Hyderabad Telengana",
"80, Bangalore Karnataka"], columns=['row'])
# Solution
df_out = df.row.str.split(',|\t', expand=True)
# Make first row as header
new_header = df_out.iloc[0]
df_out = df_out[1:]
df_out.columns = new_header


##########################################################################


import re

# Clean up spelling mistakes and deal with abbreviations
def cleanup_spelling_abbrev(text):
    replacements = [
        ['-', ', '], ['/ ', ', '], ['/', ', '], ['\(', ', '], [' and', ', '],
        [' &', ', '], ['\)', ''], [', $', ''], [',  ', ', '], [', ,', ', ']
    ]
    for i, j in replacements:
        text = re.sub(i, j, text)
    return text

df['Country'] = df['Country'].apply(cleanup_spelling_abbrev)


##########################################################################


import fuzzywuzzy
from fuzzywuzzy import process

# function to replace close matches
def replace_matches_in_column(df, column, string_to_match, min_ratio = 47):

    # get a list of unique strings
    strings = df[column].unique()
    
    # get the top 10 closest matches to our input string
    matches = fuzzywuzzy.process.extract(string_to_match, strings, 
                                         limit=10, scorer=fuzzywuzzy.fuzz.token_sort_ratio)

    # only get matches with a ratio > 90
    close_matches = [matches[0] for matches in matches if matches[1] >= min_ratio]

    # get the rows of all the close matches in our dataframe
    rows_with_matches = df[column].isin(close_matches)

    # replace all rows with close matches with the input matches 
    df.loc[rows_with_matches, column] = string_to_match
    
    # let us know the function's done
    print("All done!")

# replace close matches to "usa" with "usa"
replace_matches_in_column(df=df, column='Country', string_to_match="usa", min_ratio=70)