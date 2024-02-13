# Basic create data without extra library
import sqlite3

# Step 2: Connect to the database
conn = sqlite3.connect("sqlite_test1.db")

# Step 3: Create a cursor
cursor = conn.cursor()

# Step 4: Execute SQL command to insert data
query = "INSERT INTO users (id, username, email) VALUES (?, ?, ?)"
val = [
    (4, "patrick", "batesman@mail.com")
]

cursor.executemany(query, val)

conn.commit()

print(cursor.rowcount, "record(s) inserted successfully.")

cursor.close()
conn.close()