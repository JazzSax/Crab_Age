
import pandas as pd
from Predicting import CrabAgePredictor
from sklearn.preprocessing import StandardScaler
import sys
from os import path
from learning_model import X_train  

predictor = CrabAgePredictor()
predictor.fit_scaler(X_train)


new_data = pd.DataFrame({
    'Sex': ['I'],
    'Length': [0.7875],
    'Diameter': [0.6125],
    'Height': [0.2125],
    'Weight': [4.06815325],
    'Shucked Weight': [1.5025235],
    'Viscera Weight': [1.34660125],
    'Shell Weight': [1.417475]
})

predictions = predictor.predict_age(new_data)
final_age = str(predictions[0]) 
print("The predicted age is: " + final_age + " months.")
