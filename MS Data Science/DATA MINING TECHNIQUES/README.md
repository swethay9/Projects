# 📰 Fake News Detection Using Machine Learning  

## **Author**  
**Swetha Yanamandhalla**  
**Date**: May 5, 2024  

---

## **Project Overview**  
With the rise of misinformation, detecting fake news has become more crucial than ever. This project leverages **machine learning and natural language processing (NLP)** techniques to classify news articles as **real or fake**. Using a labeled dataset, the model analyzes text patterns and linguistic features to differentiate between trustworthy and misleading content.  

---

## **Key Features**  

✅ **Text Preprocessing & Cleaning**  
- Removing special characters, punctuation, and stopwords  
- Applying **lemmatization** to standardize words  
- Converting text to lowercase for uniformity  

✅ **Feature Engineering with TF-IDF**  
- Transforming raw text into meaningful numerical features  
- Extracting important words and phrases for classification  

✅ **Machine Learning Models for Fake News Detection**  
Implemented and compared multiple classifiers, including:  
🔹 **Logistic Regression**  
🔹 **Support Vector Machines (SVM)**  
🔹 **Naive Bayes**  
🔹 **Decision Trees & Random Forest**  
🔹 **Gradient Boosting Machines (GBM)**  
🔹 **Bagging & Bootstrapping Ensembles**  

✅ **Performance Evaluation**  
- **Confusion matrix** to analyze misclassifications  
- **Classification reports** for precision, recall, and F1-score  
- **Accuracy comparison** across different models  

---

## **Installation & Setup**  

###  **Clone the Repository**  
```bash
git clone <repository_url>
cd fake-news-detection
```

###  **Install Dependencies**  
Ensure you have Python installed, then run:  
```bash
pip install -r requirements.txt
```

###  **Dataset Setup**  
Download and place the dataset files in the appropriate directory:  
- `train.csv` → Training dataset  
- `test.csv` → Unlabeled test data  
- `submit.csv` → Labels for model evaluation  

---

## **Dataset Details**  

| Column Name | Description |
|-------------|------------|
| **text** | Full content of the news article |
| **label** | 0 = True News, 1 = Fake News |

---

## **How to Use This Project**  

### **1️⃣ Data Preprocessing**  
Run the `preprocess_text` function to clean and prepare the dataset:  
🔹 Remove noise from text  
🔹 Apply tokenization and lemmatization  
🔹 Vectorize text using **TF-IDF**  

### **2️⃣ Train Machine Learning Models**  
Experiment with different classifiers to find the best model for detecting fake news.  
```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### **3️⃣ Evaluate Performance**  
Use accuracy, precision, recall, and F1-score to measure effectiveness:  
```python
from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))
```

---

## **Results & Insights**  

 **Best-Performing Model**: Identified the most accurate classifier through rigorous testing.  
 **Feature Importance**: Analyzed which words and phrases contribute most to classification.  
 **Error Analysis**: Examined misclassified cases to improve model robustness.  

---

 ## Contributing
Contributions are welcome! If you want to contribute:
1. Fork this repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request describing your changes.

---

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

---

## Acknowledgments
- Thanks to the creators of the dataset for their efforts in data collection.
- Libraries used: `scikit-learn`, `pandas`, `matplotlib`, `nltk`, `seaborn`.
---
## Contact
For any inquiries or suggestions, feel free to reach out:
- **Name**: Swetha
- **Email**: swethachowdhary33@gmail.com
- **GitHub**: [SWETHAY9](https://github.com/swethay9)


