
import pandas as pd
from Predicting import CrabAgePredictor
from LearningModel import X_train  

class Predictor:
    def __init__(self):
        pass

    def predikt(self, sexx,  lngth,  diam,  hght,  wght,  shkwght,  vscwght,   shllwght):
        
        predictor = CrabAgePredictor()
        # predictor.fit_scaler(X_train)

        new_data = pd.DataFrame({
            'Sex': [sexx],
            'Length': [lngth],
            'Diameter': [diam],
            'Height': [hght],
            'Weight': [wght],
            'Shucked Weight': [shkwght],
            'Viscera Weight': [vscwght],
            'Shell Weight': [shllwght]
        })

        predictions = predictor.predict_age(new_data)
        final_age = str(predictions[0]) 
        
        return final_age
