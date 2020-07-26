import sqlite3
import os
import csv
import pandas as pd 

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "MLB2008.csv")
df = pd.read_csv(CSV_FILEPATH)
print(df.head())

conn = sqlite3.connect('MLBdb.sqlite3')

df.to_sql('MLB_table', conn, if_exists='append', index=False)