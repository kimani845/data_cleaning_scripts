import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# load data to notebook

cricket_df = pd.read_csv(r"C:\Users\Admin\Downloads\cricket_data.csv")
cricket_df.head(10)

# ydata for summary of the dataset general information
from ydata_profiling import ProfileReport
profile = ProfileReport(cricket_df, title  = 'cricket_visual')
profile.to_file('hello.html')

profile.to_notebook_iframe()

# check if the row has atleast one value. Retain if one value exists, and drop the whole row if both values are missing
cricket_df = cricket_df.dropna(subset = ['summary', 'content' ], thresh=1)


cricket_df.head()

cricket_df.info()


# check for duplicates 
duplicated = cricket_df['title'].duplicated().sum()
duplicated

# Indetify the duplicates based on the 'title' and keep the first occurence
cricket_df = cricket_df.duplicated(subset = ['title'], keep = 'first')

# apply the boolean mask to filter the dataframe
cricket_df = cricket_df[~cricket_df]
# (optional) reset the index if needed
cricket_df = cricket_df.reset_index(drop = True) 


dupricated=cricket_df.drop_duplicates(inplace=True)
dupricated

# the above block had an issue, beware before you run it

# print the duplicate values
# print("The duplicates are:\n", cricket_df[~cricket_df].sum())
cricket_df = cricket_df.drop_duplicates(subset=['title'])

print(cricket_df)

# splitting words
# %pip install wordninja



# using wordninja to split words
import wordninja
cricket_df["content"] = cricket_df["content"].apply(lambda x: wordninja.split(x))

cricket_df.head(10)


