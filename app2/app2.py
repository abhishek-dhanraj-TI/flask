import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="mysqldb",
    user="root",
    password="p@ssw0rd1",
    database="inventory"
  )
cursor = mydb.cursor()

@app.route('/')
def hello_world():
  return 'Hello, Docker!'

@app.route('/widgets')
def get_widgets():
  


  cursor.execute("SELECT * FROM widgets")

  row_headers=[x[0] for x in cursor.description] #this will extract row headers

  results = cursor.fetchall()
  json_data=[]
  for result in results:
    json_data.append(dict(zip(row_headers,result)))

  return json.dumps(json_data)

@app.route('/initdb')
def db_init():
  cursor.execute("DROP DATABASE IF EXISTS db")
  cursor.execute("CREATE DATABASE db")
  cursor.execute("DROP TABLE IF EXISTS person")
  cursor.execute("CREATE TABLE widgets (name VARCHAR(255), age int)")
  cursor.close()

  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')