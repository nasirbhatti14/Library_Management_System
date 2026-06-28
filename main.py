import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

conn = mysql.connector.connect(
    host = os.getenv("db_host"),
    username = os.getenv("db_username"),
    password = os.getenv("db_password"),
    database = os.getenv("db_database")
)

cursor = conn.cursor()

cursor.execute("select * from books;")

for row in cursor.fetchall():
    print(row)