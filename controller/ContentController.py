#!C:\Users\jhnbr\AppData\Local\Programs\Python\Python312\python
print("Content-Type:text/html")
print()
import cgi
import sys
from os import path

script_dir = path.dirname(path.dirname(__file__))


form = cgi.FieldStorage()
#print("<script type='text/javascript'> alert ('controlle r1');</script>")
back = form.getvalue("back")




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



if(back):
    from Functions import home
    home()
if(clear):
    from Functions import input
    input()
if (getPredict):
    from Functions import output, predict
    age = predict(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell)
    if(age <= 3):
        result = f"Crabs are not ready for harvesting. You might want to wait {6-age} for optimal harvest"
    if(age>3 and age<=5):
        result = f"Crabs are too early to be harvest. You might want to wait {6-age}"
    if(age>5 and age<=7):
        result = "Crabs are ready for harvest. Harvest now"
    if(age>7 and age <= 9):
        result = f"Crabs are past the optimal age for harvesting. But still can be harvested."
    if(age>9):
        result = f"Crabs are past harvesting. It is recommended to mate with other crab to create more crabs!"
    
    sys.path.append(script_dir)
    from model.MyQueries import MyQueries
    query = MyQueries()
    results = query.addRecord(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell,age)

    output(results,getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell,age)
    
    # input()
   

# if (getAdd):
#     c = Controller()
#     c.Add(getSex, getLength, getDiameter, getHeight, getWeight, getShucked, getViscera, getShell, getAge)