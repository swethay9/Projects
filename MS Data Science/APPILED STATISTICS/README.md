# **Applied Statistics - Final Project**  

## **About This Project**  
This repository contains R Markdown scripts for a statistical learning project focused on **regression modeling, feature selection, and performance evaluation** across different datasets. The project explores **logistic regression, Lasso regression, and polynomial regression**, applying statistical techniques to uncover patterns and make predictions.  

---

## **Project Breakdown**  

###  **1. Logistic Regression Analysis**  
- **Dataset**: `Downer` (from the `alr4` package)  
- **Goal**: Predict whether a cow will calve (`calving`) based on factors like `daysrec`, `ck`, `ast`, `urea`, and `pcv`.  
- **Steps Taken**:  
  - Cleaned and prepared the data.  
  - Split the dataset into **training and test sets**.  
  - Built a **logistic regression model** to predict calving outcomes.  
  - Assessed performance using a **confusion matrix**.  
- **Libraries Used**: `alr4`, `dplyr`, `caret`  

---

###  **2. Lasso Regression on Boston Housing Data**  
- **Dataset**: `Boston` (from the `MASS` package)  
- **Goal**: Predict the **median home value (`medv`)** based on various housing characteristics.  
- **Steps Taken**:  
  - Standardized the predictor variables.  
  - Applied **Lasso regression with cross-validation** to select the most important features.  
  - Measured model performance using **Mean Squared Error (MSE)**.  
- **Libraries Used**: `MASS`, `glmnet`  

---

###  **3. Polynomial Regression on Faithful Dataset**  
- **Dataset**: `faithful` (Old Faithful Geyser dataset)  
- **Goal**: Predict eruption duration (`eruptions`) based on waiting time (`waiting`).  
- **Steps Taken**:  
  - Built **polynomial regression models** of degrees 1 to 4.  
  - Used **10-fold cross-validation** to evaluate model performance.  
  - Selected the best polynomial degree based on **highest R² value**.  
- **Libraries Used**: `boot`  

---

## **How to Run the Project**  
###  **Step 1: Install Required Packages**  
Run this command in R to install all necessary libraries:  
```r
install.packages(c("alr4", "dplyr", "caret", "MASS", "glmnet", "boot"))
```

###  **Step 2: Load the R Markdown File**  
- Open the `.Rmd` file in **RStudio** or any R-compatible IDE.  
- Run each code chunk **sequentially** to execute the analysis.  

---

## **Project Outputs**  
🔹 **Logistic Regression**: Confusion matrix to assess prediction accuracy.  
🔹 **Lasso Regression**: Selected features and **MSE evaluation**.  
🔹 **Polynomial Regression**: Best polynomial degree for predicting eruption duration.  

---

## **About the Author**  
**Swetha Yanamandhalla**  
**Date**: December 5, 2023  

