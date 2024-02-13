# Basic update data without extra library
import sqlite3

# Step 2: Connect to the database
conn = sqlite3.connect("sqlite_test1.db")

# Step 3: Create a cursor
cursor = conn.cursor()

# Step 4: Execute SQL command to insert data
query = """
    UPDATE users SET 
        username = ?, 
        email = ?  
    WHERE id = ?"""

id = 4
username = "patrick"
email = "patrick@mail.com"

cursor.execute(query, (username, email, id,))

conn.commit()

print(cursor.rowcount, "record(s) updated successfully.")

cursor.close()
conn.close()