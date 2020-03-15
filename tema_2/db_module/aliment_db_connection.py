import sqlite3
import os


class AlimentDbConnection:
    __instance = None

    def __init__(self):
        self.db_file =  os.path.join(os.path.dirname(__file__), 'data/aliment_db.db')
        self.db_conn = None
        self.connect()
    
    @staticmethod
    def get():
        if AlimentDbConnection.__instance == None:
            AlimentDbConnection.__instance = AlimentDbConnection()

        return AlimentDbConnection.__instance
            

    def connection(self):
        return self.db_conn          

    def connect(self):
        self.db_conn

        try:
            self.db_conn = sqlite3.connect(self.db_file)
            print("Connection to db successful")
        except:
            print("Connection failed")
 
        return self