# 🕵️‍♀️ Crime Hotspots Detection Using Machine Learning

This project compares multiple machine learning algorithms to predict and identify crime hotspots based on historical crime data. It aims to assist law enforcement and city planners by forecasting areas with high crime potential based on spatial and temporal patterns.

## 📊 Overview

- **Objective**: Analyze and predict crime-prone areas using Decision Tree, Random Forest, and Naive Bayes classifiers.
- **Dataset**: Crime data collected from Kaggle (San Francisco crime dataset).
- **Tools Used**: Python, Jupyter Notebook, Matplotlib, Seaborn, Scikit-learn, Plotly

## 📁 Project Structure
├── data/
│ └── crime_dataset.csv
├── models/
│ └── decision_tree.joblib
│ └── random_forest.joblib
│ └── naive_bayes.joblib
├── notebook/
│ └── crime_analysis.ipynb
├── output/
│ └── confusion_matrices/
├── README.md

## 🔍 Methodology

1. **Data Preprocessing**
   - Removed duplicates and null values
   - Feature extraction: Extracted `month`, `day`, `hour` from datetime
   - Label encoding for categorical features

2. **Feature Selection**
   - Selected key features: `Category`, `PdDistrict`, `Month`, `Year`, `Day`, `Hour`
   - Removed redundant fields like `Description`, `Address`, `Resolution`

3. **Model Training**
   - Trained using:
     - Decision Tree
     - Random Forest
     - Naive Bayes

4. **Evaluation**
   - Accuracy
   - Confusion Matrix

## 🧪 Results

| Algorithm       | Accuracy |
|----------------|----------|
| Decision Tree  | 63%      |
| Random Forest  | 62%      |
| Naive Bayes    | 40%      |

✅ **Decision Tree** gave the best performance for this dataset.

## 📈 Visualizations

- Bar chart of major crimes
- Pie chart for district-wise crime
- Hour-wise crime frequency plots
- WordCloud of crime descriptions
- Confusion matrices for each model

## 🚀 How to Run

1. **Clone the repo:**
   git clone https://github.com/swethay9/Projects.git

2. **Install dependencies:**

bash
Copy
Edit
pip install -r requirements.txt
 3. **Launch Jupyter Notebook:**

bash
Copy
Edit
jupyter notebook
Run crime_analysis.ipynb to see full pipeline and results.

## 📌 Future Enhancements
Incorporate ARIMA for time-series crime forecasting

Integrate real-time data streams

Visualize predictions on a map using Folium or Leaflet.js

## 👩‍💻 Contributors
Swathi Prathyusha

Swetha Yanamandhalla

Sreyaaw

## License
This project is licensed under the [MIT License](LICENSE).

---

## Contact
For any inquiries or suggestions, feel free to reach out:
- **Name**: Swetha
- **Email**: swethachowdhary33@gmail.com
- **GitHub**: [SWETHAY9](https://github.com/swethay9)


