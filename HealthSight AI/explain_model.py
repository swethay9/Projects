import shap
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load dataset and model
df = pd.read_csv('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/data/patient_vitals_labeled.csv')
model = joblib.load('C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/model/risk_model.pkl')

# Process dataset
if 'blood_pressure' in df.columns:
    df[['systolic', 'diastolic']] = df['blood_pressure'].str.split('/', expand=True)
    df.drop(columns=['blood_pressure'], inplace=True)
    df['systolic'] = df['systolic'].astype(int)
    df['diastolic'] = df['diastolic'].astype(int)

df = df.drop(columns=['patient_id', 'date'])
X = df.drop(columns=['risk_label'])

# Create SHAP explainer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

# Plot feature importance
shap.summary_plot(shap_values, X, show=False)

plt.savefig("C:/Users/Sreedhar Jhansy/Desktop/HealthSight_AI_Project/model/shap_summary_plot.png")
print("✅ SHAP feature importance saved as shap_summary_plot.png")
