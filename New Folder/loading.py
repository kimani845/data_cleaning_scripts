import pandas as pd

try:
    df = pd.read_csv("football_data.csv")
except FileNotFoundError:
    print("File not found.")
    sys.exit(1)

# Ensuring all the data is a string
df['content'] = df['content'].astype(str)

#  cleaning a certain column be used  like this( for my case i tried content)

df['content'] = df['content'].apply(process_text).apply(lambda x: ' '.join(x))

df.to_csv("cleaned_data.csv")
