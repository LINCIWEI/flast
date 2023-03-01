import csv
import sqlite3
conn = sqlite3.connect('phone_data.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS deployments')
conn.execute('CREATE TABLE deployments (Brand TEXT,model TEXT,colour TEXT,original_price INTEGER,discounted_price INTEGER,ratings REAL,rating_count INTEGER)')
print("table created successfully")
with open('phone_data/flipkart_smartphones.csv', newline='',errors='ignore') as f:
    reader = csv.reader(f,delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        Brand = (row[0])
        model = (row[1])
        colour = (row[2])
        original_price = (row[3])
        discounted_price = (row[4])
        ratings = (row[5])
        rating_count = (row[6])

        cur.execute('INSERT INTO deployments VALUES(?,?,?,?,?,?,?)',(Brand,model,colour,original_price,discounted_price,ratings,rating_count))
        conn.commit()
print("data parsed successfully")
