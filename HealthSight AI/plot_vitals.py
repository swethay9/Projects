import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv(r'C:\Users\Sreedhar Jhansy\Desktop\HealthSight_AI_Project\data\patient_vitals_cleaned.csv')

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Get unique patient IDs
patients = df['patient_id'].unique()

# Limit to first 3 patients for demo (you can remove this line to do all)
patients = patients[:3]

# Plot for each patient
for patient in patients:
    patient_df = df[df['patient_id'] == patient]

    plt.figure(figsize=(10, 5))
    plt.plot(patient_df['date'], patient_df['heart_rate'], marker='o', label='Heart Rate')
    plt.plot(patient_df['date'], patient_df['systolic'], marker='x', label='Systolic BP')
    plt.plot(patient_df['date'], patient_df['glucose_level'], marker='s', label='Glucose Level')

    plt.title(f'Vitals Over Time – {patient}')
    plt.xlabel('Date')
    plt.ylabel('Measurement')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
