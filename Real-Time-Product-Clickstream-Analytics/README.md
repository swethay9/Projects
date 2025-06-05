# Real-Time Product Clickstream Analytics with Kafka, Spark & Airflow

🚀 This project simulates a real-time clickstream analytics pipeline—similar to those used in e-commerce platforms—for capturing, processing, and visualizing user behavior.

---

## 🧠 Architecture Overview

**Pipeline Flow:**
Kafka → Spark Structured Streaming → Parquet/CSV → Airflow DAGs → Flask Dashboard + Tableau Reports

---

## ⚙️ Technologies Used
- **Apache Kafka** – Click event ingestion
- **Apache Spark (PySpark)** – Real-time stream processing with window aggregations
- **Apache Airflow** – Job orchestration and automation
- **Flask + Plotly** – Interactive real-time dashboard
- **Tableau** – Visual analytics and trend exploration
- **Parquet/CSV** – Data storage

---

## 🔍 Key Features
- Kafka producer generates product click events
- Spark processes streaming data in 10-second time windows
- Airflow DAG schedules ETL workflows
- Final results saved in Parquet and CSV
- Flask + Plotly dashboard for live insights
- Tableau dashboard for post-analysis

---
## ✅ How to Run

Tested locally on **Windows + Ubuntu WSL**. You can simulate the full stack locally.

---



## 📁 **Repository Structure**
pgsql
Copy
Edit
├── kafka_producer/        → Python Kafka producer for click events  
├── spark_streaming/       → PySpark Structured Streaming script  
├── airflow_dags/          → Airflow DAG to orchestrate stream jobs  
├── flask_dashboard/       → Flask app to show real-time insights  
├── data/                  → Output data in Parquet/CSV  
├── tableau_dashboard/     → Tableau visuals/snapshots  
├── requirements.txt       → Python dependencies  
└── README.md              → Project overview  
## 📊 **Demo Dashboard**
🔹 Flask Dashboard – Sample Visuals



## 🚀 **Upload Your Code to GitHub**
If not already pushed, follow these commands:

bash
Copy
Edit
cd Real-Time-Product-Clickstream-Analytics
git init
git remote add origin https://github.com/yourusername/Real-Time-Product-Clickstream-Analytics.git
git add .
git commit -m "Initial commit: Real-time product clickstream analytics project"
git push -u origin main
## 📝 **License**
This project is licensed under the MIT License.

## 📬 **Contact**
For any inquiries or suggestions, feel free to reach out:

Name: Swetha

Email: swethachowdhary33@gmail.com

GitHub: SWETHAY9

