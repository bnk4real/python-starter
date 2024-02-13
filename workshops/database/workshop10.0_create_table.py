# Basic create table connect database without extra library
import sqlite3

# Step 2: Connect to the database (create if not exists)
conn = sqlite3.connect("sqlite_test.db")

# Step 3: Create a cursor
cursor = conn.cursor()

# Step 4: Execute SQL command to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);
"""
cursor.execute(create_table_query)

# Step 5: Commit changes and close the connection
conn.commit()
conn.close()

print("Database created successfully.")