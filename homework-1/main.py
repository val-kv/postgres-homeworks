"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv
import psycopg2

# Connect to the database
conn = psycopg2.connect(database="north", user="val_k", password="1986", host="localhost", port="5432")
cur = conn.cursor()

# Read and insert data from customers_data.csv
with open('north_data/customers_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row[0], row[1], row[2]))

# Read and insert data from employees_data.csv
with open('north_data/employees_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))

# Read and insert data from orders_data.csv
with open('north_data/orders_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4]))

# Commit the changes and close the connection
conn.commit()
conn.close()
