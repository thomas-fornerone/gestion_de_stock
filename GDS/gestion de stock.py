import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "ThZbg57!",
  database = "boutique"
)
cur = db.cursor()
cur.execute("show tables;")
for x in cur:
  print(x)