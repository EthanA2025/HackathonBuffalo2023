import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler

# load your dataset
df = pd.read_csv('student_data.csv')
df = df.drop('student_id', axis=1)
# split the dataset into features (X) and target (y)
X = df[[f'gpa_year_{i+1}' for i in range(8)]]
y = df['dropout']
df = df.drop('dropout', axis=1)
#X = df[[f'gpa_year_{i+1}' for i in range(8)]]
X = np.array(df.mean(axis=1)).reshape(-1, 1)
scaler = StandardScaler()
X = scaler.fit_transform(X)


# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(y_train.shape)
# create the logistic regression model
model = LogisticRegression()
# train the model
model.fit(X_train, y_train)

# test the model
y_pred = model.predict(X_test)

# print the classification report
print(classification_report(y_test, y_pred))