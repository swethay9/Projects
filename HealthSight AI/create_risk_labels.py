import pandas as pd

# Load your cleaned vitals dataset
df = pd.read_csv('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/data/patient_vitals.csv')

# Split blood pressure
df[['systolic', 'diastolic']] = df['blood_pressure'].str.split('/', expand=True)
df['systolic'] = df['systolic'].astype(int)
df['diastolic'] = df['diastolic'].astype(int)

# Create risk label: 1 = High Risk, 0 = Normal
df['risk_label'] = ((df['glucose_level'] > 140) | (df['sleep_hours'] < 5)).astype(int)

# Save to new CSV
df.to_csv('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/data/patient_vitals_labeled.csv', index=False)

print("✅ Risk labels added and saved.")
