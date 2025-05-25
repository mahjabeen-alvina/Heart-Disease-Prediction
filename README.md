Heart Disease Prediction App
This is an AI-powered app that predicts the likelihood of heart disease in a person using machine learning models. It primarily uses a logistic regression model that achieves 76% accuracy in prediction.
About the Project
Heart disease is a leading cause of death globally. Early prediction based on key health parameters can help in timely medical intervention and lifestyle changes. This project uses machine learning to analyze important medical data and predict heart disease risk.
Machine Learning Models Used
We experimented with two popular classification algorithms:
Logistic Regression
- A statistical method used for binary classification problems.
- It estimates the probability of a binary response (heart disease present or not) based on input features.
- Logistic regression models the relationship between the dependent binary variable and one or more independent variables by using a logistic function.
Random Forest
- An ensemble learning method that builds multiple decision trees and merges their results.
- It improves accuracy by reducing overfitting common in single decision trees.
- Random forest handles non-linear relationships and feature interactions well.
Model Performance
Model	Accuracy	Precision	Recall	F1 Score
Logistic Regression	76%	0.78	0.75	0.76
Random Forest	73%	0.74	0.72	0.73
Confusion Matrices
Logistic Regression
	Predicted No	Predicted Yes
Actual No	40	13
Actual Yes	10	37
Random Forest
	Predicted No	Predicted Yes
Actual No	38	15
Actual Yes	12	35
Input Parameters and Their Importance
Parameter	Description	Why It Matters
Age	Age of the patient in years	Heart disease risk increases with age.
Sex	Gender of the patient (1 = male, 0 = female)	Gender affects the prevalence and type of heart disease.
Chest Pain Type	Type of chest pain experienced (e.g., typical angina)	Different types indicate different heart conditions.
Resting Blood Pressure	Blood pressure at rest (mm Hg)	High blood pressure strains the heart.
Serum Cholesterol	Cholesterol level in mg/dl	High cholesterol is a major risk factor.
Fasting Blood Sugar	Whether fasting blood sugar is > 120 mg/dl (1 = true; 0 = false)	Diabetes and blood sugar levels impact heart health.
Resting ECG Results	Results of resting electrocardiogram	Shows heart rhythm and electrical activity.
Maximum Heart Rate Achieved	Peak heart rate during exercise	Lower max HR can indicate poor cardiovascular fitness.
Exercise Induced Angina	Presence of chest pain during exercise (1 = yes; 0 = no)	Indicates heart stress under exertion.
ST Depression	ST segment depression induced by exercise relative to rest	Reflects abnormalities in heart muscle function.
Slope of ST Segment	Slope of the peak exercise ST segment	Helps evaluate the severity of heart disease.
Number of Major Vessels	Number of major vessels colored by fluoroscopy (0-3)	Indicates narrowing/blockage in arteries.
Thalassemia	Blood disorder status (3 = normal; 6 = fixed defect; 7 = reversible defect)	Affects oxygen transport in blood, impacting heart function.
Why We Use Logistic Regression
Although both logistic regression and random forest models performed well, logistic regression showed slightly better accuracy and balanced precision-recall in this case. Additionally, logistic regression offers better interpretability, which is crucial in healthcare applications for understanding how each parameter impacts the prediction.
How to Use
1. Enter the required health information in the app interface.
2. Click Predict.
3. The app outputs whether the subject is likely to have heart disease.
4. If the prediction indicates risk, it is recommended to consult a healthcare professional for further evaluation.
