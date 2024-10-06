import pyodbc
from exception import DBConnectionException
from util.DBPropertyUtil import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_db_connection():
        connection_string = DBPropertyUtil.get_connection_string("db_config.properties")
        try:
            connection = pyodbc.connect(connection_string)
            return connection
        except pyodbc.Error as e:
            raise DBConnectionException(str(e))

