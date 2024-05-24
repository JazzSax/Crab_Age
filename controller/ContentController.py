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
    def __init__(self, sex, length, diameter, height, weight, shucked, viscera, shell, age):
        self.sex = sex
        self.length = length
        self.diameter = diameter
        self.height = height
        self.weight = weight
        self.shucked = shucked
        self.viscera = viscera
        self.shell = shell
        self.age = age

    def Add(self):
        sys.path.append(script_dir + "/model/")    
        #print(f"<script type='text/javascript'> alert ('{self.age}');</script>")
        from MyQueries import MyQueries 
        mq = MyQueries()
        message = mq.addRecord(self.sex, self.length, self.diameter, self.height, self.weight, self.shucked, self.viscera, self.shell, self.age)
        print(f"<script type='text/javascript'> alert ('{message}');</script>")

    # def ShowAll():
    #     from MyQueries import MyQueries as mq
    #     mq.showAll()
    
    # def ShowOutput():
    #     from MyQueries import MyQueries as mq
    #     mq.showOutput()


# From fields
getSex = form.getvalue("sex")
getLength = form.getvalue("length")
getDiameter = form.getvalue("diameter")
getHeight = form.getvalue("height")
getWeight = form.getvalue("weight")
getShucked = form.getvalue("shucked_weight")
getViscera = form.getvalue("viscera_weight")
getShell = form.getvalue("shell_weight")
#getAge = form.getWeight("age")

# from buttons
getPredict = form.getvalue("join")
# getShowAll = form.getvalue("all")
# getShowOutput = form.getvalue("output")

if (getPredict):
    #print("<script type='text/javascript'> alert ('if');</script>")
    c = Controller(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, "10")
    c.Add()

# if str(getShowAll) != "None":
#     from MyController import Controller as c
#     c.ShowAll()

# if str(getShowOutput) != "None":
#     from MyController import Controller as c
#     c.ShowOutput()

