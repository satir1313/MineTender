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

    def close_connection(self):
        self.db_connection.close()
        
    ### create reuired database in the first run the app
    def create_database(self):   
        try:           
            exists = self.check_table_exists("Equipment")
            if not exists:
                self.cursor.execute("""CREATE TABLE Equipment (
                                id int IDENTITY(1,1) NOT NULL,
                                name varchar(255),
                                brand varchar(255),
                                year int,
                                capacity float,
                                consumption float);""")
                self.cursor.commit()
                print("Database is created!")
            else:
                print('Database already exists')
        except Exception as e:
            print("Database is not created!")
            print(e)
            
    ### check whether table already exist in the database        
    def check_table_exists(self, tablename):
        self.cursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if self.cursor.fetchone()[0] == 1:
            return True

        return False

    # insert values in a table
    # param{ table name, column names, values to insert}
    def db_insert(self, table, cols, vals):
        query_cols = ""
        values = ""
        
        for col_name in cols:
            query_cols += col_name + ","
        query_cols = query_cols[:len(query_cols)-1] 
        
        for val in vals:
            values += "'{0}',".format(val)
        values = values[:len(values)-1]
        
        query = "INSERT INTO {0}".format(table) + "(" + query_cols + ") VALUES (" + values + ")"
        self.cursor.execute(query)
        self.cursor.commit()
        
    # return values from databse table    
    def db_get(self, table, id):
        data = []
        query = "SELECT * FROM {0} WHERE id = {1}".format(table, id)
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    
cols = ['name', 'brand', 'year', 'capacity', 'consumption']
vals = ['Digger', 'CAT', '2019', '150', '150']
       

db = db_context()
db.create_database()
db.db_insert('Equipment', cols, vals)
db.db_get('Equipment', 2)

# if __name__ == "__main__":   
#     db = db_context()
#     db.db_connect()
    