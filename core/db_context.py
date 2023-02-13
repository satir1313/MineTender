import sqlite3

class DB_context:
    connection = None
    cursor = None
    
    def __init__(self, path):
        try:
            self.connection = sqlite3.connect(f'{path}\MineTender.db')
            self.cursor = self.connection.cursor()
        except Exception as e:
            print('Connection to database failed wit error: {0}'.format(e))
            
    def create_tables(self):
        res = self.cursor.execute("SELECT name FROM sqlite_master")
        tables = res.fetchone()

        if tables is None or "Equipment" not in tables:           
            self.cursor.execute("""CREATE TABLE Equipment (
                                    id INTEGER PRIMARY KEY,
                                    name text NOT NULL,
                                    brand text NOT NULL,
                                    year int,
                                    capacity float,
                                    consumption float)""")
            self.connection.commit()
        else:
            print('Table already exists.')
            
    def get_all(self, table):
        query = 'select * from {0}'.format(table)
        res = self.cursor.execute(query)
        result = res.fetchall()
        return result
        
    def get_by_id(self, table, id):
        query = 'SELECT * FROM {0} WHERE id = {1}'.format(table, id)
        res = self.cursor.execute(query)
        result = res.fetchone()
        return result
    
    def insert(self, table, cols, values):
        query = """
                    INSERT INTO {0} {1} VALUES {2}
                """.format(table, cols, values)
        self.cursor.execute(query)
        self.connection.commit()
        
    def delete_by_id(self, table, id):
        query = 'DELETE FROM {0} WHERE id = {1}'.format(table, id)
        self.cursor.execute(query)
        self.connection.commit()
        
    def close(self):
        self.connection.close()
        
if __name__ == "__main__":
    db = DB_context()
