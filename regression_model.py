import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

# load your dataset
# let's assume the data has two columns: "GPA" and "dropout" (1 if the student dropped out, 0 otherwise)
df = pd.read_csv('student_data.csv')

# split the dataset into features (X) and target (y)
X = df[[f'gpa_year_{i+1}' for i in range(8)]]
y = df['dropout']

# it's a good practice to scale the features so they have a mean of 0 and standard deviation of 1
scaler = StandardScaler()
X = scaler.fit_transform(X)

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# create the logistic regression model
model = LogisticRegression()

# train the model
model.fit(X_train, y_train)

# test the model
y_pred = model.predict(X_test)

# print the classification report
print(classification_report(y_test, y_pred))