# 🩺 HealthSight AI – Predictive Health Risk Monitoring

**Contributors**: Swetha Yanamandhalla, Ajaychary Kandukuri  
🔗 [Live Dashboard (Power BI)](https://bit.ly/HealthSightDashboard)

---

## 📘 Project Overview

**HealthSight AI** is a full-stack healthcare data project that simulates patient vitals, predicts health risks using machine learning, explains predictions with SHAP, and visualizes insights in Power BI.

This project covers **Data Engineering**, **Data Science**, and **Data Analytics** workflows.

---

## 🔍 Problem Statement

Early detection of health risks can save lives. Our project simulates real-world vitals data for 50 patients over 20 days and identifies potential high-risk individuals based on critical health indicators.

---

## 🧩 Technologies Used

| Role            | Tools                                |
|-----------------|--------------------------------------|
| Data Engineer   | Python, PostgreSQL, pandas, psycopg2 |
| Data Scientist  | scikit-learn, SHAP                   |
| Data Analyst    | Power BI, SQL                        |

---

## 🗂️ Dataset Details

- **Records**: 1,000
- **Patients**: 50 (P001–P050)
- **Vitals**:
  - `heart_rate`
  - `blood_pressure` (split into `systolic`, `diastolic`)
  - `glucose_level`
  - `sleep_hours`
  - `risk_flag` (0 = normal, 1 = high-risk)

---

## ⚙️ Project Structure

HealthSight_AI_Project/
│
├── data/
│ └── patient_vitals.csv
│
├── scripts/
│ ├── load_data.py
│ ├── clean_data.py
│ ├── create_table.py
│ ├── load_to_postgres.py
│ ├── train_model.py
│ ├── explain_model.py
│
├── images/
│ └── Dashboard.png
│
├── dashboard/
│ └── HealthSight_Dashboard.pbix
│
├── README.md
└── requirements.txt

---

## 🚀 Key Features

### ✅ ETL Pipeline  
- Cleaned vitals from CSV → PostgreSQL  
- Parsed date, split blood pressure, created `risk_flag`

### ✅ Machine Learning  
- Trained Random Forest classifier  
- Predicts risk based on vitals  
- Achieved 100% accuracy on simulated data

### ✅ Explainability with SHAP  
- Interprets model output  
- Visualizes feature impact on predictions

### ✅ Power BI Dashboard  
![Dashboard](https://github.com/user-attachments/assets/ad0f7b5a-5cfb-4561-827c-b87414ccbded)


- 📈 Vitals Line Chart (glucose, heart rate, sleep)
- 📊 Risk Flag Bar Chart (red = high risk, blue = normal)
- 💡 KPI Cards: Avg. glucose, sleep, % high-risk
- 📅 Date Slicer to filter charts

---

## 📌 Business Impact

This simulation mimics a real-world predictive health system:
- Alerts clinicians to risky patterns  
- Helps stakeholders track population health  
- Scales with real-time data using ETL and dashboards

---

## 🧠 Skills Demonstrated

- Data Engineering: ETL, SQL, PostgreSQL
- Data Science: Classification, SHAP explainability
- Data Analytics: Power BI, business KPI reporting

---

## 📤 Deploy & Extend

### Optional:
- Convert ML to Flask API  
- Automate pipeline with Airflow  
- Store data in AWS S3 + Redshift

---



## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For any inquiries or suggestions, feel free to reach out:
- **Name**: Swetha
- **Email**: swethachowdhary33@gmail.com
- **GitHub**: [SWETHAY9](https://github.com/swethay9)
