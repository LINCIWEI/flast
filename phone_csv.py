import csv
import sqlite3
import decimal
from datetime import datetime
conn = sqlite3.connect('bar_data.db',detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS barsize')
conn.execute('DROP TABLE IF EXISTS barlist')
conn.execute('CREATE TABLE barsize ('
             'Cost_storage TEXT,'
             'Cost_bottle TEXT,'
             'Cost_transportation TEXT,'
             'Percentage_markup TEXT,'
             'Discount_percentage TEXT,'
             'Size TEXT PRIMARY KEY )')
conn.execute('CREATE TABLE barlist ('
             'Vendor_code TEXT PRIMARY KEY,'
             'Name TEXT ,'
             'Retail_price TEXT,'
             'Base_unit TEXT,'
             'Country_of_Origin TEXT,'
             'ratings TEXT,'
             'ABV TEXT,'
             'Size TEXT,'
             'FOREIGN KEY(Size) REFERENCES barsize(size))')

print("table created successfully")
with open('phone_data/Product_range (1).csv', newline='',errors='ignore') as f:
    reader = csv.reader(f,delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        Vendor_code= (row[0])
        Name = (row[1])
        Retail_price = (row[2])
        Base_unit = (row[3])
        Country_of = (row[4])
        ratings = (row[5])
        ABV = (row[6])
        Size = (row[7])

        cur.execute('INSERT INTO barlist VALUES(?,?,?,?,?,?,?,?)',(Vendor_code,Name,Retail_price,Base_unit,Country_of,ratings,ABV,Size))
        conn.commit()

with open('phone_data/Transactions.csv', newline='',errors='ignore') as f:
    reader = csv.reader(f,delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        Cost_storage= (row[0])
        Cost_bottle = (row[1])
        Cost_transportation = (row[2])
        Percentage_markup = (row[3])
        Discount_percentage = (row[4])
        Size = (row[5])
        cur.execute('INSERT INTO barsize VALUES(?,?,?,?,?,?)',(Cost_storage,Cost_bottle,Cost_transportation,Percentage_markup,Discount_percentage,Size))
        conn.commit()

print("data parsed successfully")
