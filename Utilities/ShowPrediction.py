
import pandas as pd
from Utilities.Predicting import CrabAgePredictor
from Utilities.LearningModel import X_train  


class Prediction:
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
       
        predictor = CrabAgePredictor()
        predictor.fit_scaler(X_train)

       
        new_data = pd.DataFrame({
            'Sex': [self.sex],
            'Length': [self.length],
            'Diameter': [self.diameter],
            'Height': [self.height],
            'Weight': [self.weight],
            'Shucked Weight': [self.shucked],
            'Viscera Weight': [self.viscera],
            'Shell Weight': [self.shell]
        })

        predictions = predictor.predict_age(new_data)
        final_age = str(predictions[0]) 
       
        return final_age


