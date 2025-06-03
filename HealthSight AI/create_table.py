import psycopg2

# PostgreSQL connection details
conn = psycopg2.connect(
    dbname="healthsight",
    user="postgres",
    password="postgres",  # Update if needed
    host="localhost",
    port="5432"
)

# Create cursor
cur = conn.cursor()

# SQL to create the table
create_table_query = '''
CREATE TABLE IF NOT EXISTS patient_vitals (
    patient_id VARCHAR(10),
    date DATE,
    heart_rate INT,
    glucose_level INT,
    sleep_hours FLOAT,
    systolic INT,
    diastolic INT
);
'''

# Execute and commit
cur.execute(create_table_query)
conn.commit()

print("✅ Table 'patient_vitals' created successfully.")


# Close connection
cur.close()
conn.close()
