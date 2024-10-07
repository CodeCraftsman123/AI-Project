import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Load the dataset
file_path = 'E:\\Programming\\AIProject\\hypothyroid_label_encoded_mean_imputed_shuffled.csv'
df = pd.read_csv(file_path)

# Splitting the data into features (X) and target (y)
X = df.drop(columns=['result'])  # All columns except the target 'result'
y = df['result']  # The target variable

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize logistic regression model
logreg = LogisticRegression(max_iter=1000)

# Train the model
logreg.fit(X_train, y_train)

# Make predictions on the test data
y_pred = logreg.predict(X_test)

# Calculate metrics
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred) * 100  # Convert to percentage
precision = precision_score(y_test, y_pred) * 100  # Convert to percentage
recall = recall_score(y_test, y_pred) * 100  # Sensitivity, convert to percentage
f1 = f1_score(y_test, y_pred) * 100  # Convert to percentage

# Calculate specificity
tn, fp, fn, tp = conf_matrix.ravel()
specificity = (tn / (tn + fp)) * 100  # Convert to percentage

# Print the labeled confusion matrix
print("Confusion Matrix:")
print(f"TN = {tn}, FP = {fp}")
print(f"FN = {fn}, TP = {tp}")

# Print results
print(f"Accuracy: {accuracy:.2f}%")
print(f"Precision: {precision:.2f}%")
print(f"F1-Score: {f1:.2f}%")
print(f"Specificity: {specificity:.2f}%")
print(f"Sensitivity (Recall): {recall:.2f}%")