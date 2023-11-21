import mysql.connector
import tkinter
import request
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="MySQL@12345",
  database="dav"
)
mycursor = mydb.cursor()

class user:
    def __init__(self,username,password,grade):
        self.username=username
        self.password=password
        self.grade=grade
    def store(self):
        a=(self.username,self.password,self.grade)
        query="insert into learnquest values(%s,%s,%s)"
        mycursor.execute(query,a)
        mydb.commit()
    def check(self):
        exists=False
        mycursor.execute('select * from learnquest')
        a=mycursor.fetchall()
        for x in a:
            if self.username in x[0]:
                exists=True
        return exists
uvan=user("uvanrishee","open@123",12)
if uvan.check() :
    print('already exist')
else:
    uvan.store()

        
        
