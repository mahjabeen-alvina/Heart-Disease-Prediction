import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("heart.csv")  # Adjust filename if needed
print(df.head())
df.info()
df.describe()
df.isnull().sum()
sns.countplot(x='condition', data=df)
# Clean up column names just in case
df.columns = df.columns.str.strip()
plt.title("Heart Disease Diagnosis Count")
plt.xlabel("0 = No Disease | 1 = Disease")
plt.ylabel("Number of Patients")
plt.show()
print(df['condition'].value_counts())
# Convert to binary (0 = No disease, 1 = Any heart disease)
df['condition'] = df['condition'].apply(lambda x: 1 if x > 0 else 0)
# Step 1: Prepare Features and Labels
X = df.drop('condition', axis=1)  # Features
y = df['condition']               # Target/Label
# Step 2: Split the data into Training and Testing sets

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# Step 3: Train a Logistic Regression Model
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Step 4: Evaluate the Model
y_pred = model.predict(X_test)
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=["No Disease", "Disease"], yticklabels=["No Disease", "Disease"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
joblib.dump(model, 'heart_disease_model.pkl')
print("Model saved successfully!")



