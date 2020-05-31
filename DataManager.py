import mysql.connector
import datetime
from dotenv import load_dotenv
import os

class DataManager   :

   dbname = ''
   tables = []

   def __init__(self, dbname):
      self.dbname = dbname
      self.host     = os.getenv("db_host")
      self.user     = os.getenv("db_user")
      self.passwd   = os.getenv("db_passwd")
      self.port     = os.getenv("db_port")

   def init(self):
     print ("Check DB status... ")
     self.connect()
     dbFound = self.checkIfDatabaseExist()

     # Create DB
     if dbFound == False:
         print(' No DB Found')
         self.cursor.execute("CREATE DATABASE " + self.dbname)
         print('  db created')

     else:
         print(" DB %s Found" %(self.dbname))

     # USE DB
     self.cursor.execute("USE " + self.dbname)
     print(' USE DB ' + self.dbname)
     self.getTables()

   def connect(self):
      self.db = mysql.connector.connect(
        host=self.host,
        user=self.user,
        passwd=self.passwd,
        port=self.port
      )
      self.cursor = self.db.cursor()

   def checkIfDatabaseExist(self):
     self.cursor.execute("SHOW DATABASES")
     dbFound = False
     for x in self.cursor:
       if x[0] == self.dbname:
         dbFound = True

     return dbFound



   def getTables(self):
       print('Get Tables')
       self.tables = []
       self.cursor.execute("SHOW TABLES")
       for x in self.cursor:
        	self.tables.append(x[0])

   def initMarket(self, name):
       if name in self.tables:
           print("Table for market %s found" %(name))
       else:
           print("Oups... Table for market %s not found" %(name))
           self.createMarketTable(name)

   def createMarketTable(self, name):
       print("Create market table %s " %(name))
       self.cursor.execute('CREATE TABLE ' + name + """ (
        id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        price FLOAT(16)
       ) """)

   def insertMartketData(self, market, price):
        sql = "INSERT INTO " + market + " (price) VALUES ( " + price + ")"
        val = (price)
        self.cursor.execute(sql)
        self.db.commit()
