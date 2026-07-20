import mysql.connector
import os

def ping_database():
    conn = mysql.connector.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USERNAME"),
        port = os.getenv("DB_PORT"),
        password = os.getenv("DB_PASSWORD"),
        database = os.getenv("DB_DATABASE"),
        ssl_ca = "ca.pem",
        ssl_verify_cert = True,
        
    )

    cursor = conn.cursor()
    cursor.execute("SELECT 1;")
    cursor.fetchone()
    cursor.close()
    conn.close()
    print("Database pinged successfully — still active.")

if __name__ == "__main__":
    ping_database()