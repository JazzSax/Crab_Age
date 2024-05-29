#!C:\Users\jhnbr\AppData\Local\Programs\Python\Python312\python
print("Content-Type:text/html")
print()
import cgi
import sys
from os import path

script_dir = path.dirname(path.dirname(__file__))


form = cgi.FieldStorage()
#print("<script type='text/javascript'> alert ('controlle r1');</script>")





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
clear = form.getvalue("clear")
back = form.getvalue("back")


if(back):
    from Functions import home
    home()
if(clear):
    from Functions import input
    input()
if (getPredict):
    from Functions import output, predict
    age = predict(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell)
    sys.path.append(script_dir)
    from model.MyQueries import MyQueries
    query = MyQueries()
    result = query.addRecord(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell,age)

    output(result,getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell,age)
    
    # input()
   

# if (getAdd):
#     c = Controller()
#     c.Add(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, getAge)