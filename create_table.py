# create_table.py
import psycopg2

# Replace with your actual DB credentials
conn = psycopg2.connect(
    host="your_host",
    database="your_db",
    user="your_user",
    password="your_password"
)

cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()
cur.close()
conn.close()
