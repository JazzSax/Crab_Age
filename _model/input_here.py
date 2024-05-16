
import pandas as pd
from Predicting import CrabAgePredictor
from sklearn.preprocessing import StandardScaler
import sys
from os import path
from learning_model import X_train  

predictor = CrabAgePredictor()
predictor.fit_scaler(X_train)


new_data = pd.DataFrame({
    'Sex': ['F'],
    'Length': [1.55],
    'Diameter': [1.2125],
    'Height': [0.4375],
    'Weight': [34.45881725],
    'Shucked Weight': [15.4504775],
    'Viscera Weight': [7.1724235],
    'Shell Weight': [9.7805775]
})

predictions = predictor.predict_age(new_data)
final_age = str(predictions[0]) 
print("The predicted age is: " + final_age + " months.")
