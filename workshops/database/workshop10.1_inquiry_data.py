# basic inquiry data
import sqlite3

# Step 2: Connect to the database (create if not exists)
conn = sqlite3.connect("sqlite_test1.db")

# Step 3: Create a cursor
cursor = conn.cursor()

# Step 4: Execute SQL command to create a table
query = "SELECT id, username, email FROM users;"
cursor.execute(query)
rows = cursor.fetchall()

# Print the retrieved data
for row in rows:
    if len(row) != 0:
        print(row)

conn.close()