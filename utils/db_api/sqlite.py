from datetime import datetime
import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

   
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())


   # ------- table -------------------------------------------
    def insert_user(self, user_id, full_name, username, status):
        return self.execute('INSERT INTO users (user_id, full_name, username, status) VALUES(?,?,?,?)', 
                            (user_id, full_name, username, status), commit=True) 
    
    def get_user(self, user_id):
        return self.execute('SELECT * FROM users WHERE user_id=?', (user_id,), fetchone=True)


def logger(statement):
    print(f"Executing: {statement}")
