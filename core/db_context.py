import os
from dotenv import load_dotenv
import pyodbc

class db_context:
    db_connection = None
    cursor = None
    def __init__(self):
        load_dotenv()
        try:
            connection_strings = os.getenv('CONNECTION_STRINGS')
            self.db_connection = pyodbc.connect(connection_strings)
            self.cursor = self.db_connection.cursor()
        except:
            print("Connection to databse failed!")

    ### create reuired database in the first run the app
    def create_database(self):
        try:           
            exists = self.check_table_exists("Equipment")
            if not exists:
                self.cursor.execute("""CREATE TABLE Equipment (
                                id INT NOT NULL,
                                name VARCHAR(255),
                                brand VARCHAR(255),
                                year INT,
                                capacity DECIMAL,
                                concumption DECIMAL,
                                PRIMARY KEY(id));""")
                self.cursor.commit()
                print("Database is created!")
            else:
                print('Database already exists')
                # close connection anyway
                self.db_connection.close()
        except:
            print("Database is not created!")
            
    ### check whether table already exist in the database        
    def check_table_exists(self, tablename):
        self.cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if self.cursor.fetchone()[0] == 1:
            self.cursor.close()
            return True

        self.cursor.close()
        return False

    def db_insert(self):
        self.cursor.execute("""INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
                                VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway'); """)

        
        

db = db_context()
db.create_database()

# if __name__ == "__main__":   
#     db = db_context()
#     db.db_connect()
    