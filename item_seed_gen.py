import pandas as pd

df = pd.read_csv("chardb.csv")

print(
    """INSERT INTO characters
    (title,
    first_name,
    last_name)
    VALUES"""
)
for index, row in df.iterrows():
    print(
        f"""('{row['title']}',
    '{row['first_name']}',
    '{row['last_name']}'),"""
    )
