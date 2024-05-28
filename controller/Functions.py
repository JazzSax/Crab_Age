import sys
import os
script_dir = os.path.dirname(os.path.dirname(__file__))

def getAll():
     sys.path.append(script_dir + "/model/")
     from MyQueries import MyQueries
     mq = MyQueries()
     allRecords = mq.showAll()
     # for i in allRecords:
     #      for j in i:
     #           print(j, "=", i[j])
     return allRecords

def view():
    allRecords = getAll()
    sys.path.append(script_dir + "/view/")    
    print("<script type='text/javascript'> alert ('functions');</script>")
    from Views import Views
    view = Views()    
    view.viewAll(allRecords)

def input():
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showForm()

def output(sex, length, diameter, height, weight, shucked, viscera, shell, age):
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showOutput(sex, length, diameter, height, weight, shucked, viscera, shell, age)
