import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split 

# Read the data
data = pd.read_csv(r"D:\workspace\DataAnalytics\DAy13\Bank Customer Churn Prediction.csv")

# Drop rows with missing values
data = data.dropna()

# Define features and target variable
features = ["country", "gender", "products_number", "credit_card", "active_member"]
target = "churn"

# Encode categorical features
encoder = LabelEncoder()
for col in features:
  if data[col].dtype == object:
    data[col] = encoder.fit_transform(data[col])

# Scale numeric feature (Age)
scaler = StandardScaler()
data["credit_score"] = scaler.fit_transform(data[["credit_score"]])
data["age"] = scaler.fit_transform(data[["age"]])
data["balance"] = scaler.fit_transform(data[["balance"]])
data["estimated_salary"] = scaler.fit_transform(data[["estimated_salary"]])

# Separate features and target
X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1) # 70% training and 30% test

# Create decision tree classifier
model = DecisionTreeClassifier()

# Train the model
model = model.fit(X_train,y_train)

y_pred = model.predict(X_test)

from sklearn import metrics 
from sklearn.metrics import confusion_matrix

# Print various classification metrics
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
print("Precision:", metrics.precision_score(y_test, y_pred))
print("Recall:", metrics.recall_score(y_test, y_pred))
print("F1-score:", metrics.f1_score(y_test, y_pred))
print("Classification report:\n", metrics.classification_report(y_test, y_pred))

# Print the importance of each feature
print("Feature importances:")
for feature, importance in zip(features, model.feature_importances_):
  print(f"{feature}: {importance:.2f}")

# Make predictions (commented out for now)
# Assuming you have a separate test dataset with similar structure as 'data'
# test_data = pd.read_csv("titanic_test.csv")  # Replace with your test data path
# predictions = model.predict(test_data[features])

# Save the tree as an image
# Two options

# Option 1 - Create a dot file and then convert manually to png format
# Save the tree as a DOT file
#with open("titanic_tree.dot", "w") as f:
#  export_graphviz(model, out_file=f, feature_names=features, filled=True)
# You will then have to say dot -Tpng titanic_tree.dot -o titanic_tree.png to convert


# Option 2 - Directly create a png file
from sklearn.tree import export_graphviz
from io import StringIO  
from IPython.display import Image  
import pydotplus
dot_data = StringIO()
export_graphviz(model, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = features,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('bank.png')
Image(graph.create_png())
