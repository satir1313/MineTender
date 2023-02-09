import os
from dotenv import load_dotenv
import pyodbc

class db_context:
    def __init__(self):
        load_dotenv()
        pass

    def db_connect(self):
        try:
            connection_strings = os.getenv('CONNECTION_STRINGS')
            connection = pyodbc.connect(connection_strings)
            self.create_database(connection)
            return True
        except:
            print("Connection to databse failed!")
            return False


    ### create reuired database in the first run the app
    def create_database(self, connection):
        try:
            cursor = connection.cursor()
            exists = self.check_table_exists(connection, "Equipment")
            if not exists:
                cursor.execute("""CREATE TABLE Equipment (
                                id INT NOT NULL,
                                name VARCHAR(255),
                                brand VARCHAR(255),
                                year INT,
                                capacity DECIMAL,
                                concumption DECIMAL,
                                PRIMARY KEY(id));""")
                cursor.commit()
                print("Database is created!")
            else:
                print('Database already exists')
                # close connection anyway
                connection.close()
        except:
            print("Database is not created!")
            
    ### check whether table already exist in the database        
    def check_table_exists(self, dbcon, tablename):
        dbcur = dbcon.cursor()
        dbcur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True

        dbcur.close()
        return False


db = db_context()
db.db_connect()

# if __name__ == "__main__":   
#     db = db_context()
#     db.db_connect()
    