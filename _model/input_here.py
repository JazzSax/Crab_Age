
print("<script type='text/javascript'> alert ('predict class 0.0');</script>")
import pandas as pd
print("<script type='text/javascript'> alert ('predict class 0.1');</script>")
from Predicting import CrabAgePredictor
print("<script type='text/javascript'> alert ('predict class 0.2');</script>")
from sklearn.preprocessing import StandardScaler
import sys
from os import path
from learning_model import X_train  

class input():

    def predikt(self, sexx,  lngth,  diam,  hght,  wght,  shkwght,  vscwght,   shllwght):
        print("<script type='text/javascript'> alert ('predict class 1');</script>")
        predictor = CrabAgePredictor()
        predictor.fit_scaler(X_train)

        print("<script type='text/javascript'> alert ('predict class 2');</script>")
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
        print("The predicted age is: " + final_age + " months.")
        return final_age
