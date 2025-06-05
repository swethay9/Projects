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

### Step-by-Step Instructions

#### 1️⃣ Start Kafka Services (on Windows)
Start **Zookeeper** and **Kafka server**:

```bash
.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties
.\bin\windows\kafka-server-start.bat .\config\server.properties
2️⃣ Run Kafka Producer (on Windows)
Sends simulated product click events to Kafka topic:

bash
Copy
Edit
python3 kafka_producer.py
3️⃣ Run Spark Structured Streaming Consumer (on Ubuntu/WSL)
Consumes Kafka stream, aggregates data, and saves as Parquet and CSV:

bash
Copy
Edit
spark-submit spark_streaming_consumer.py
4️⃣ Start Apache Airflow Scheduler (on Ubuntu/WSL)
Schedules or triggers the Spark job via Airflow DAG:

bash
Copy
Edit
source ~/airflow_env/bin/activate
airflow scheduler
5️⃣ Launch Flask Dashboard (on Ubuntu/WSL)
Reads Parquet files and displays insights:

bash
Copy
Edit
python3 app.py
Then open your browser and go to:
http://localhost:5000

## 📁 Repository Structure

kafka_producer/ → Python Kafka producer for click events
├── spark_streaming/ → PySpark Structured Streaming script
├── airflow_dags/ → Airflow DAG to orchestrate stream jobs
├── flask_dashboard/ → Flask app to show real-time insights
├── data/ → Output data in Parquet/CSV
├── tableau_dashboard/ → Tableau visuals/snapshots
├── requirements.txt → Python dependencies
├── README.md → Project overview

---



📊 Demo Dashboard

![Flask With BS Dashboard1](https://github.com/user-attachments/assets/09a75ee8-bbab-4f50-893b-6ba1ba4fcfa5)
![Flask with BS Dashboard2](https://github.com/user-attachments/assets/c0568145-ff26-4cfe-a27e-1c9cc33f786d)





###  **Upload Your Code to GitHub**
If not already pushed:
```bash
cd Real-Time-Product-Clickstream-Analytics
git init
git remote add origin https://github.com/yourusername/Real-Time-Product-Clickstream-Analytics.git
git add .
git commit -m "Initial commit: Real-time product clickstream analytics project"
git push -u origin main

