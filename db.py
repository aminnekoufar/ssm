import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="M@dar123456",
  database="ssm"
)

def sql(qure):

    mycursor = mydb.cursor()
    mycursor.execute(qure)
    return mycursor.fetchall()
