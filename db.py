import sqlite3

# Connect to the database
conn = sqlite3.connect("soilerosion.db")
print("Opened database successfully")

# Create tables
conn.execute("CREATE TABLE IF NOT EXISTS adminlogin (ausername varchar, apassword varchar)")
conn.execute("CREATE TABLE IF NOT EXISTS faq (question varchar, answer varchar)")
conn.execute("CREATE TABLE IF NOT EXISTS signup (uname varchar, uphone varchar, username varchar, upassword varchar)")
print("Tables created successfully")

# Insert default admin details
default_admin_username = "admin@admin.com"
default_admin_password = "123456"

conn.execute("INSERT INTO adminlogin (ausername, apassword) VALUES (?, ?)", (default_admin_username, default_admin_password))
print("Default admin details added successfully")

# Commit the transaction and close the connection
conn.commit()
conn.close()
print("Database connection closed")
