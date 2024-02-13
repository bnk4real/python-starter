# Basic delete data without extra library
import sqlite3

# Step 2: Connect to the database
conn = sqlite3.connect("sqlite_test1.db")

# Step 3: Create a cursor
cursor = conn.cursor()

# Step 4: Execute SQL command to delete data
query = "DELETE FROM users WHERE id = ?"

id = 4
cursor.execute(query, (id,))

conn.commit()

print(cursor.rowcount, "record deleted successfully.")

cursor.close()
conn.close()