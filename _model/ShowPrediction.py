
import pandas as pd
from Predicting import CrabAgePredictor
from sklearn.preprocessing import StandardScaler
import sys
from os import path
from learning_model import X_train  

print("<script type='text/javascript'> alert ('prediction file');</script>")

class Prediction():
    def __init__(self, sex, length, diameter, height, weight, shucked, viscera, shell):
        self.sex = sex
        self.length = length
        self.diameter = diameter
        self.height = height
        self.weight = weight
        self.shucked = shucked
        self.viscera = viscera
        self.shell = shell
    
    def GetPrediction(self):
        print(f"<script type='text/javascript'> alert ('prediction started');</script>")
        predictor = CrabAgePredictor()
        predictor.fit_scaler(X_train)


        new_data = pd.DataFrame({
            'Sex': str(self.sex),
            'Length': int(self.length),
            'Diameter': int(self.diameter),
            'Height': int(self.height),
            'Weight': int(self.weight),
            'Shucked Weight': int(self.shucked),
            'Viscera Weight': int(self.viscera),
            'Shell Weight': int(self.shell)
        })

        predictions = predictor.predict_age(new_data)
        final_age = str(predictions[0]) 
        print(f"<script type='text/javascript'> alert ('The predicted age is: {final_age} months.');</script>")
        return final_age
