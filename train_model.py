import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load dataset
data = pd.read_csv("Income_Expense_Data.csv")

print("Dataset Preview:")
print(data.head())

# Check missing values
print("\nMissing values:")
print(data.isnull().sum())

# Handle missing values
data['Income'] = data['Income'].fillna(data['Income'].median())
data['Age'] = data['Age'].fillna(data['Age'].median())
data['Expense'] = data['Expense'].fillna(data['Expense'].median())

# Features and target
X = data[['Income', 'Age']]
y = data['Expense']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open("model.pkl", "wb"))

print("\nModel trained successfully and saved as model.pkl")