import pandas as pd

# Load original data
df = pd.read_csv(r'C:\Users\Sreedhar Jhansy\Desktop\HealthSight_AI_Project\data\patient_vitals.csv')

# Split blood pressure
df[['systolic', 'diastolic']] = df['blood_pressure'].str.split('/', expand=True)

# Convert to proper data types
df['systolic'] = pd.to_numeric(df['systolic'], errors='coerce')
df['diastolic'] = pd.to_numeric(df['diastolic'], errors='coerce')
df['heart_rate'] = pd.to_numeric(df['heart_rate'], errors='coerce')
df['glucose_level'] = pd.to_numeric(df['glucose_level'], errors='coerce')
df['sleep_hours'] = pd.to_numeric(df['sleep_hours'], errors='coerce')
df['date'] = pd.to_datetime(df['date'], dayfirst=True)

# Drop original blood pressure column
df.drop(columns=['blood_pressure'], inplace=True)

# Save cleaned version
df.to_csv(r'C:\Users\Sreedhar Jhansy\Desktop\HealthSight_AI_Project\data\patient_vitals_cleaned.csv', index=False)

# Preview data
print("✅ Data cleaned and saved.")
print("\n📊 Cleaned Data Preview:")
print(df.head())

print("\n🔎 Missing values:")
print(df.isnull().sum())
