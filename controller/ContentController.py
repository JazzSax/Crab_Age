#!/Python37/python
print("Content-Type: text/html")
print()
import cgi
import sys
import os

script_dir = os.path.dirname(os.path.dirname(__file__))


form = cgi.FieldStorage()
#print("<script type='text/javascript'> alert ('controlle r1');</script>")

class Controller():
    def __init__(self):
        # self.sex = sex
        # self.length = length
        # self.diameter = diameter
        # self.height = height
        # self.weight = weight
        # self.shucked = shucked
        # self.viscera = viscera
        # self.shell = shell
        # self.age = age
        pass

    def Show(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):        
        from Functions import output
        output(sex, length, diameter, height, weight, shucked, viscera, shell, age)

    def Predict(self, sex, length, diameter, height, weight, shucked, viscera, shell):
        print("<script type='text/javascript'> alert ('Predict method');</script>")
        sys.path.append(script_dir + "/_model/")
        from ShowPrediction import Prediction
        p = Prediction(sex, length, diameter, height, weight, shucked, viscera, shell)
        age = int(p.GetPrediction())
        #print(f"<script type='text/javascript'> alert ('{age}');</script>")
        return age
    

# From fields
getSex = form.getvalue("sex")
getLength = form.getvalue("length")
getDiameter = form.getvalue("diameter")
getHeight = form.getvalue("height")
getWeight = form.getvalue("weight")
getShucked = form.getvalue("shucked_weight")
getViscera = form.getvalue("viscera_weight")
getShell = form.getvalue("shell_weight")

# from buttons
getPredict = form.getvalue("predict")

if (getPredict):
    print("<script type='text/javascript'> alert ('if');</script>")
    c = Controller()
    age = c.Predict(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell)
    c.Show(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, age) #show prediction to user

