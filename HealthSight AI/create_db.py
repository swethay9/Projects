import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Replace with your credentials
host = "localhost"
port = "5432"
user = "postgres"
password = "postgres"  # <-- update if you changed it

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname="postgres",
        user=user,
        password=password,
        host=host,
        port=port
    )

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Create new database
    cursor.execute("CREATE DATABASE healthsight;")
    print("✅ Database 'healthsight' created successfully.")

    cursor.close()
    conn.close()

except Exception as e:
    print("❌ Error:", e)
