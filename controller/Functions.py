
import sys
import os


script_dir = os.path.dirname(os.path.dirname(__file__))

def home():
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.home()

def getAll():

     sys.path.append(script_dir)
     from model.MyQueries import MyQueries
     query = MyQueries()
     allRecords = query.showAll()
     return allRecords

def view():
    allRecords = getAll()
    sys.path.append(script_dir + "/view/")    
    from Views import Views
    view = Views()    
    view.viewAll(allRecords)

def input():
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showForm()

def output(res,result,sex, length, diameter, height, weight, shucked, viscera, shell, age):
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.showOutput(res,result,sex, length, diameter, height, weight, shucked, viscera, shell, age)

    

# def Add(sex, length, diameter, height, weight, shucked, viscera, shell, age):
#      sys.path.append(script_dir + "/model/")    
#      #print(f"<script type='text/javascript'> alert ('{self.age}');</script>")
#      from MyQueries import MyQueries 
#      mq = MyQueries()
#      message = mq.addRecord(sex, length, diameter, height, weight, shucked, viscera, shell, age)
#      #print(f"<script type='text/javascript'> alert ('{message}');</script>")



def predict(sexx, lngth, diam, hght, wght, shkwght, vscwght, shllwght):
    try:
          
          sys.path.append(script_dir)
          from models.ShowPrediction import Prediction
          i = Prediction(sexx, lngth, diam, hght, wght, shkwght, vscwght, shllwght)
          age = i.GetPrediction()
          
          return age

    except ImportError as e:
        print(f"An error occurred during import: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def search(input):
     sys.path.append(script_dir)
     from model.MyQueries import MyQueries
     query = MyQueries()
     searched = query.showResult(input)
     sys.path.append(script_dir + "/view/")
     from Views import Views
     view = Views()
     view.search(searched)