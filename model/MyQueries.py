from model.MyConnection import MyConnection


class MyQueries: 
        
        def __init__(self) :
                self.conn = MyConnection("localhost","root","","crab")
                self.mydb = self.conn.connect()
        
        def addRecord(self, sex, length, diameter, height, weight, shucked, viscera, shell,age ):
              
                mycursor = self.mydb.cursor()
                sql = "INSERT INTO info (sex,length,diameter,height,weight,shucked,viscera,shell, age) VALUES ('"+str(sex)+"','"+str(length)+"','"+str(diameter)+"','"+str(height)+"','"+str(weight)+"','"+str(shucked)+"','"+str(viscera)+"','"+str(shell)+"','"+str(age)+"')"
                #sql = "INSERT INTO info (sex,length,diameter,height,weight,shucked,viscera,shell, age) VALUES ('1','1','1','1','1','1','1','1','1')"
                mycursor.execute(sql)
                self.mydb.commit()
                result=mycursor.rowcount, "Record Added!"  
                return result
               
        def showAll(self):
                myCursor = self.mydb.cursor(dictionary=True)
                myCursor.execute("Select * From info")
                result = myCursor.fetchall()
                return result
        def showResult(self,input):
                mycursor = self.mydb.cursor(dictionary=True)
                mycursor.execute("SELECT * FROM info WHERE age='"+input+"' or sex='"+input+"'" )
                myresult = mycursor.fetchall()
                return myresult


        

       