import psycopg2
import pandas as pd

# Load the cleaned CSV file
df = pd.read_csv('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/data/patient_vitals.csv')


# Split blood_pressure into systolic and diastolic
df[['systolic', 'diastolic']] = df['blood_pressure'].str.split('/', expand=True)
df.drop(columns=['blood_pressure'], inplace=True)

# Convert types
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df['systolic'] = df['systolic'].astype(int)
df['diastolic'] = df['diastolic'].astype(int)

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="healthsight",
    user="postgres",
    password="postgres",  # update if different
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# Insert each row into the table
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO patient_vitals (patient_id, date, heart_rate, glucose_level, sleep_hours, systolic, diastolic)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        row['patient_id'],
        row['date'],
        row['heart_rate'],
        row['glucose_level'],
        row['sleep_hours'],
        row['systolic'],
        row['diastolic']
    ))

conn.commit()
cur.close()
conn.close()

print("✅ Data loaded into PostgreSQL successfully.")
