#__path__ = "C:/xampp/htdocs/source/IT140P/Crab_Age/model/"

print("Content-Type: text/html")
print()
import cgi
#import sys

form = cgi.FieldStorage()

# From fields
getSex = form.getvalue("sex")
getLength = form.getvalue("length")
getDiameter = form.getvalue("diameter")
getHeight = form.getvalue("height")
getWeight = form.getWeight("weight")
getShucked = form.getvalue("shucked-weight")
getViscera = form.getvalue("viscera-weight")
getShell = form.getvalue("shell-weight")
getAge = form.getWeight("age")

# from buttons
getAdd = form.getvalue("add")
getShowAll = form.getvalue("all")
getShowOutput = form.getvalue("output")

if str(getAdd) != "None":
    from MyController import Controller as c
    c.Add(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, getAge)

if str(getShowAll) != "None":
    from MyController import Controller as c
    c.ShowAll()

if str(getShowOutput) != "None":
    from MyController import Controller as c
    c.ShowOutput()

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
        #sys.path.append(__path__)
        from model import MyQueries as mq
        message = mq.MyQueries.addRecord(self.sex, self.length, self.diameter, self.height, self.weight, self.shucked, self.viscera, self.shell, self.age)
        print(message)

    def ShowAll():
        from model import MyQueries as mq
        mq.MyQueries.showAll()
    
    def ShowOutput():
        from model import MyQueries as mq
        mq.MyQueries.showOutput()


