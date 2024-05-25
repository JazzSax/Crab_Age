import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load
import sys
from os import path
from learning_model import X_train  
class CrabAgePredictor:
    def __init__(self, model_path=r'C:\xampp\htdocs\source\IT140P\Crab_Age\trained_model.joblib'):
        self.model = load(model_path)
        self.scaler = None  

    def fit_scaler(self, X):
        self.scaler = StandardScaler()
        self.scaler.fit(X) 

    def preprocess_data(self, data):
        if self.scaler is None:
            raise ValueError("Scaler is not fitted. Call 'fit_scaler' method before preprocessing data.")
        
        # Add dummy columns for 'Sex' feature
        data_encoded = pd.get_dummies(data, columns=['Sex'], drop_first=True)
        
        # Ensure the columns are in the same order as X_train
        data_encoded = data_encoded.reindex(columns=X_train.columns, fill_value=0)
        
        return self.scaler.transform(data_encoded)

    def predict_age(self, data):
        processed_data = self.preprocess_data(data)
        predictions = self.model.predict(processed_data)
        return predictions


