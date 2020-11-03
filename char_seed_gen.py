import pandas as pd
import psycopg2

df = pd.read_csv("chardb.csv")

print('''INSERT INTO characters
    (title,
    first_name,
    last_name,
    public_description,
    private_description_cover_story,
    private_description_truth,
    starting_information_other_characters,
    starting_information_hints,
    character_secret,
    character_clue,
    primary_goal,
    secondary_goal,
    tertiary_goal
    )
    VALUES''')
for index,row in df.iterrows():
    try:
        print(f'''('{row['title']}',
        '{row['first_name']}',
        '{row['last_name']}',
        '{row['public_description']}',
        '{row['private_description_cover_story']}',
        '{psycopg2.extensions.QuotedString(row['private_description_truth'])}',
        '{psycopg2.extensions.QuotedString(row['starting_information_other_characters'])}',
        '{psycopg2.extensions.QuotedString(row['starting_information_hints'])}',
        '{row['character_secret']}',
        '{row['character_clue']}',
        '{row['primary_goal']}',
        '{row['secondary_goal']}',
        '{row['tertiary_goal']}'
        ),''')
    except:
        print(f'''('{row['title']}',
        '{row['first_name']}',
        '{row['last_name']}',
        '{row['public_description']}',
        '{row['private_description_cover_story']}',
        '{row['private_description_truth']}',
        '{row['starting_information_other_characters']}',
        '{row['starting_information_hints']}',
        '{row['character_secret']}',
        '{row['character_clue']}',
        '{row['primary_goal']}',
        '{row['secondary_goal']}',
        '{row['tertiary_goal']}'
        ),''')

