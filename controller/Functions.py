import sys
import os
script_dir = os.path.dirname(os.path.dirname(__file__))


def view():
    sys.path.append(script_dir + "/view/")    
    #print("<script type='text/javascript'> alert ('functions');</script>")
    from Views import Views
    view = Views()    
    view.viewAll()

def input():
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showForm()

def output(sex, length, diameter, height, weight, shucked, viscera, shell, age):
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showPrediction(sex, length, diameter, height, weight, shucked, viscera, shell, age)
