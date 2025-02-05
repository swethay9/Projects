# Author
Swetha Yanamandhalla
Date: March 13, 2024
Project Description
This project applies statistical learning techniques to analyze and predict miles per gallon (mpg) for different car models using the Auto dataset from the ISLR package. The study explores relationships between vehicle attributes such as horsepower, weight, and cylinders and their impact on fuel efficiency. Several machine learning models, including Linear Regression, Decision Trees, and Random Forests, were used to make predictions and assess model performance.

The analysis includes:

Data Cleaning and Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering and Selection
Predictive Modeling using Statistical Learning Methods
Model Performance Evaluation
Data Preprocessing
Dataset Overview:

The Auto dataset consists of 392 rows and 9 columns with vehicle attributes such as mpg, horsepower, weight, and acceleration.
Handling Missing Values:

Checked for missing values using colSums(is.na(dataset_name)), and no missing values were found.
Data Splitting:

Training Set: 70% of the data
Test Set: 30% of the data
Stratified sampling was used to ensure a balanced distribution of the target variable (mpg).
Exploratory Data Analysis (EDA)
Histograms: Distribution of mpg showed a right-skewed pattern with a peak around 20 mpg.
Scatter Plots: Relationships between mpg and other variables:
Negative correlation with horsepower, weight, and cylinders.
Vehicles with more cylinders and higher horsepower tend to have lower mpg.
Box Plots: Identified outliers in mpg and weight.
Correlation Matrix:
Strong negative correlation between mpg and weight (-0.83) and mpg and horsepower (-0.78).
Feature Engineering and Statistical Learning Methods
Feature Transformation:

Log transformations applied to horsepower, weight, and acceleration to normalize distributions.
Feature Selection:

LASSO Regression was used to select the most relevant predictors.
Interaction terms (horsepower × weight, horsepower × acceleration) were introduced.
Predictive Models Used:

Linear Regression
Decision Tree
Random Forest
Model Training and Evaluation
Linear Regression Model
Model trained on mpg using predictors: log_horsepower, log_weight, and interaction terms.
R-squared: 0.714 (indicating moderate predictive power).
Root Mean Squared Error (RMSE): 4.26.
Cross-validation improved R-squared to 0.807.
Random Forest Model
Best-performing model with R-squared: 0.846 and RMSE: 3.07.
Cross-validation confirmed stable results.
Decision Tree Model
Performed worse than other models (R-squared: 0.632, RMSE: 4.75).
Overfitting observed, leading to poor generalization.
Model Comparison
Model	RMSE	R²	Accuracy
Linear Regression	4.26	0.714	83.2%
Random Forest	3.07	0.846	91.9%
Decision Tree	4.75	0.632	79.5%
Conclusion: The Random Forest model outperformed all others, achieving the highest accuracy and lowest RMSE.

Required Libraries
The following R libraries were used:

ggplot2
caret
caTools
randomForest
glmnet
How to Run the Project
Install required libraries:
r
Copy
Edit
install.packages(c("ggplot2", "caret", "caTools", "randomForest", "glmnet"))
Load the dataset and run the preprocessing steps.
Train and evaluate the models using the provided script.
Results and Conclusions
Key Findings:

Weight and horsepower are strong predictors of mpg.
Random Forest model achieved the best prediction performance.
Decision Tree model had the lowest accuracy due to overfitting.
Scope and Generalizability:

The model provides valuable insights into vehicle fuel efficiency.
Can be extended to newer datasets with more recent car models.
Limitations & Future Improvements:

Dataset represents older vehicle models and may not generalize to modern cars.
Feature engineering could be enhanced by including additional predictors (e.g., aerodynamics, fuel type).
Deep learning models could be explored for better performance.
Output
Visualizations: Scatter plots, histograms, and model performance graphs.
Model Performance: R-squared, RMSE, MAE, and accuracy scores.
