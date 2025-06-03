import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load labeled data
df = pd.read_csv('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/data/patient_vitals_labeled.csv')

# ❗ Split blood pressure again (if not split already)
if 'blood_pressure' in df.columns:
    df[['systolic', 'diastolic']] = df['blood_pressure'].str.split('/', expand=True)
    df['systolic'] = df['systolic'].astype(int)
    df['diastolic'] = df['diastolic'].astype(int)
    df.drop(columns=['blood_pressure'], inplace=True)

# Drop unnecessary columns
df = df.drop(columns=['patient_id', 'date'])

# Define features and target
X = df.drop(columns=['risk_label'])
y = df['risk_label']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("✅ Model trained. Evaluation:")
print(classification_report(y_test, y_pred))

# Save model
joblib.dump(model, 'C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/model/risk_model.pkl')
