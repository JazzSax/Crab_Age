import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump
import os



script_dir = os.path.dirname(__file__)

csv_path = os.path.join(script_dir, 'CrabAgePrediction.csv')

df = pd.read_csv(csv_path)
df = pd.get_dummies(df, columns=['Sex'], drop_first=True, dtype=int)

X = df.drop('Age', axis=1)
y = df['Age']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
model = RandomForestRegressor(random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)


dump(model, 'trained_model.joblib')
