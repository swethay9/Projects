# 🚖 NYC Taxi Trip Analysis & Visualization  

## **Author**  
**Swetha Yanamandhalla**  
 **Date**: May 5, 2024  

## **Project Overview**  
This project delves into the **spatial and temporal trends** of NYC's Yellow Cab services using 2016 trip records. By analyzing millions of rides, we uncover **patterns in taxi usage, peak travel times, and hotspot locations**. The project utilizes **machine learning, clustering, and visualization techniques** to provide a deeper understanding of urban mobility in New York City.  

---  

## **Table of Contents**  

- [Introduction](#introduction)  
- [Dataset Details](#dataset-details)  
- [Setup & Installation](#setup--installation)  
- [Key Features](#key-features)  
- [Visual Insights](#visual-insights)  
- [Clustering Analysis](#clustering-analysis)  
- [How to Use](#how-to-use)  
- [Findings & Results](#findings--results)  
- [Credits & Acknowledgments](#credits--acknowledgments)  

---

## **Introduction**  
Ever wondered how **New Yorkers move around using taxis**? This project breaks down **millions of cab rides** to reveal interesting trends in trip duration, frequency, and locations. We explore **when, where, and how people use taxis**, providing an in-depth look at urban mobility through **maps, time-based trends, and clustering techniques**.  

---

## **Dataset Details**  

The project is based on real-world **NYC Yellow Cab trip data from 2016**, containing:  
🔹 **1.4M+ trips in the training set** (`train.csv`)  
🔹 **600K+ trips in the test set** (`test.csv`)  
🔹 **A sample submission file** (`sample_submission.csv`)  

### **Key Data Fields**  
📍 **Pickup & Drop-off Info**: Latitude/Longitude coordinates  
🕒 **Timestamps**: Start & end times of trips  
👥 **Passenger Count**: How many riders per trip  
⏳ **Trip Duration**: Travel time in seconds  

---

## **Setup & Installation**  

### **Clone the Repository**  
```bash
git clone <repository-url>
cd nyc-taxi-trip-analysis
```

### **Install Dependencies**  
```bash
pip install -r requirements.txt
```

---

## **Key Features**  

✅ **Data Cleaning & Preprocessing**: Filtering out extreme values and errors  
✅ **Trip Duration Analysis**: Understanding ride time variations  
✅ **Spatial Density Mapping**: Identifying NYC’s busiest pickup & drop-off zones  
✅ **Temporal Usage Trends**: Exploring peak and off-peak taxi demand  
✅ **Clustering Trips**: Grouping similar rides to uncover travel patterns  

---

## **Visual Insights**  

🔹 **Trip Duration Distribution**: Histogram analysis of short vs. long rides  
🔹 **Heatmaps**: Where taxis are busiest in NYC  
🔹 **Time-Based Analysis**: Peak hours, weekday vs. weekend trends  
🔹 **Manhattan Travel Patterns**: Focused breakdown of cab activity  
🔹 **Clustering Visuals**: Mapping grouped trip behaviors across NYC  

---

## **Clustering Analysis**  

- **Goal**: Identify **typical NYC taxi routes**  
- **Attributes Used**:  
  📍 Pickup & Drop-off Locations  
  ⏳ Trip Duration  
- **Algorithm**: MiniBatch **K-Means (80 clusters)**  
- **Outcome**: Groups of **common taxi routes**, helping uncover daily commuter and leisure travel behaviors  

---

## **How to Use**  

### **Run the Analysis & Generate Visuals**  
1️⃣ Ensure your dataset files are in the `data/` folder  
2️⃣ Run the main script:  
```bash
python nyc_taxi_analysis.py
```
3️⃣ The script will generate **trip maps, heatmaps, and trend graphs**  

### **Launch the GUI to View Results**  
To interactively explore visual outputs, run:  
```bash
python gui_showcase.py
```

---

## **Findings & Results**  

📅 **Taxi Demand by Time**  
- 🚗 **Weekdays are busier than weekends**  
- ⏰ **Peak hours**: Morning rush (7-9 AM) & evening commute (5-8 PM)  

📍 **Spatial Insights**  
- 🌆 **Manhattan dominates taxi activity**  
- 🛑 High-density drop-offs near **airports, business districts, and tourist spots**  

🗺 **Clustering Insights**  
- **80 trip clusters identified** 📊  
- Revealed common routes for **business commuters, airport transfers, and nightlife travelers**  

---

## **Credits & Acknowledgments**  

🗂 **Data Source**: NYC Taxi and Limousine Commission (TLC)  
📊 **Inspiration**: Open-source transportation datasets & visualization tools  

---

