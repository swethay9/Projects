

# **Computational Statistics - Final Project**

## **Author**  
**Swetha Yanamandhalla**  
**Date**: October 19, 2023  

---

## **Project Description**  
This project analyzes sales trends and consumer behavior using the **Global Superstore Dataset**. The objective is to identify key patterns in sales, customer loyalty, and the impact of discounts through data-driven statistical and machine learning techniques.

The analysis includes:
1. **Data Cleaning and Preprocessing**  
2. **Exploratory Data Analysis (EDA)**  
3. **Correlation Analysis**  
4. **Chi-Square Tests for Categorical Variables**  
5. **Logistic Regression Modeling for Sales Prediction**  

---

## **Data Preprocessing**  
1. **Missing Values**:  
   - Checked and removed missing values using `na.omit()`.  
2. **Duplicate Records**:  
   - Identified and removed duplicate entries.  
3. **Data Type Conversion**:  
   - Converted categorical variables and date-time formats for analysis.  

---

## **Exploratory Data Analysis (EDA)**  
- **Histograms**: Distribution of Sales, Yearly Trends.  
- **Bar Charts**: Sales by Product Category and City.  
- **Correlation Matrix**: Identified relationships between numerical variables.  

---

## **Statistical Analysis**  
1. **Correlation Analysis**  
   - A correlation matrix was computed for numerical features such as `Sales`, `Profit`, `Discount`, and `Quantity`.  
2. **Chi-Square Tests**  
   - Tested associations between sales and categorical factors (`Category`, `City`, `Country`, `Customer Name`).  

---

## **Logistic Regression Model**  
1. **Dataset Split**  
   - Training: 80%  
   - Testing: 20%  

2. **Model Fitting**  
   - A logistic regression model was trained with **Sales** as the dependent variable and **Year** as the independent variable.  
   - Model Accuracy: **100%** (Potential overfitting due to data imbalance).  

3. **Confusion Matrix & ROC Curve**  
   - A confusion matrix was generated, but model performance needs improvement due to class imbalance.  

---

## **Results**  
- **Key Findings**:  
  - Sales trends were analyzed using logistic regression but need refinement with additional features.  
  - Correlation analysis showed significant relationships between sales, discount, and profit.  
  - Chi-square tests revealed associations between sales and categorical factors.  
- **Model Performance**:  
  - Accuracy: **100%** (needs further validation).  
  - Correlation and chi-square tests provided insights into sales dynamics.  

---

## **Required Libraries**  
The following R libraries were used:  
- `ggplot2`  
- `caret`  
- `caTools`  
- `ROCR`  

---

## **How to Run the Project**  
1. Download the dataset (`superstore.csv`) and update the file path in the script.  
2. Install the required R libraries using:  
   ```r
   install.packages(c("ggplot2", "caret", "caTools", "ROCR"))
   ```
3. Run the R Markdown script in RStudio to generate the report and visualizations.  

---

## **Output**  
- **Visualizations**: Sales distributions, yearly trends, correlation heatmaps.  
- **Model Performance**: Confusion matrix, accuracy, recall, precision, and AUC evaluation.  

---
## Contact
For any inquiries or suggestions, feel free to reach out:
- **Name**: Swetha
- **Email**: swethachowdhary33@gmail.com
- **GitHub**: [SWETHAY9](https://github.com/swethay9)



