import cgi, mysql.connector
from flask import request

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password='',
  database="OmnifoodDB"
)

form = cgi.FieldStorage()

name = form.getvalue("name")
email = form.getvalue("email")
find = form.getvalue("find-us")
news = form.getvalue("news")
message = form.getvalue("message")

cur = mydb.cursor()
cur.execute("INSERT INTO omnofoodtb (name, email, find, news, message) VALUES (%s, %s, %s, %s, %s)", (name, email, find, news, message))
mydb.commit()

cur.close()
mydb.close()