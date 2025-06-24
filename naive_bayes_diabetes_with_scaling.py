import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("diabetes.csv")

# Define columns for scaling
standard_scaler_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'DiabetesPedigreeFunction', 'Age']
min_max_scaler_cols = ['SkinThickness', 'Insulin', 'BMI']

# Standard Scaling
standard_scaler = StandardScaler()
df[standard_scaler_cols] = standard_scaler.fit_transform(df[standard_scaler_cols])

# Min-Max Scaling
min_max_scaler = MinMaxScaler()
df[min_max_scaler_cols] = min_max_scaler.fit_transform(df[min_max_scaler_cols])

# Display all columns temporarily
pd.set_option('display.max_columns', None)
print(df.head())
pd.reset_option("display.max_columns")

# Features and target
X = df.drop('Outcome', axis=1)
y = df['Outcome']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Display metrics
print("Model Performance Metrics:")
print(f"  Accuracy: {accuracy:.2f}")
print(f"  Precision: {precision:.2f}")
print(f"  Recall: {recall:.2f}")
print(f"  F1 Score: {f1:.2f}\n")

print("Classification Report:")
print(classification_report(y_test, y_pred))

# Confusion matrix
plt.figure(figsize=(6, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=["No Diabetes", "Diabetes"], yticklabels=["No Diabetes", "Diabetes"])
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Display predicted vs actual for the test set
print("\nPredicted vs Actual Outcomes (Test Set):")
for actual, predicted in zip(y_test, y_pred):
    print(f"  Actual: {actual}, Predicted: {predicted}")
