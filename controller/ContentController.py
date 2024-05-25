#!/Python37/python
print("Content-Type: text/html")
print()
import cgi
import sys
from os import path

script_dir = path.dirname(path.dirname(__file__))


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

    def Add(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        sys.path.append(script_dir + "/model/")    
        #print(f"<script type='text/javascript'> alert ('{self.age}');</script>")
        from MyQueries import MyQueries 
        mq = MyQueries()
        message = mq.addRecord(sex, length, diameter, height, weight, shucked, viscera, shell, age)
        #print(f"<script type='text/javascript'> alert ('{message}');</script>")

    def Show(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        from Functions import output
        output(sex, length, diameter, height, weight, shucked, viscera, shell, age) # pass parameters for output


    def Predict(self, sexx,  lngth,  diam,  hght,  wght,  shkwght,  vscwght,   shllwght):
        #print("<script type='text/javascript'> alert ('predict method 1');</script>")
        sys.path.append(script_dir + "/_model/")
        from input_here import input 
        i = input()
        #print("<script type='text/javascript'> alert ('predict method 2');</script>")
        age = int(i.predikt(sexx,  lngth,  diam,  hght,  wght,  shkwght,  vscwght,   shllwght))
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
getAge = form.getvalue("age")

# from buttons
getPredict = form.getvalue("predict")
getAdd = form.getvalue("add")

if (getPredict):
    #print("<script type='text/javascript'> alert ('if');</script>")
    c = Controller()
    age = c.Predict(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell)
    c.Show(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, age) # show output

if (getAdd):
    c = Controller()
    c.Add(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, getAge)