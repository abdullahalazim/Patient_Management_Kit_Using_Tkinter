'''
Copyright (c) 2023 Abdullah Al Azim
'''

# run this file only one time
import sqlite3

conn = sqlite3.connect('patient_db.db')
c = conn.cursor()
c.execute("""CREATE TABLE patient(
  p_id text,
  name text,
  age text,
  gender text,
  phone_no text,
  location text
)""")

conn.commit()
conn.close()