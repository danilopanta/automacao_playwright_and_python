import pyodbc
from pytests.support.log_service import LogService

LOG = LogService

class SqlServerUtils:

    def connection_sql_server(params):
        try:
            connection_string = (
                f"DRIVER={{SQL Server}};"
                f"SERVER={params['host']},{params['port']};"
                f"DATABASE={params['database']};"
                f"UID={params['user']};"
                f"PWD={params['password']};"
            )
            connection = pyodbc.connect(connection_string)
        except Exception as e:
            LOG.log_error(f"Erro ao conectar no Banco: {e}")
            connection = None
        return connection

    def query_sql_server(connection, query):
        results = []
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            col_names = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                result = dict(zip(col_names, row))
                results.append(result)
            cursor.close()
            LOG.log_info(f"Query realizada: {results}")
        except Exception as e:
            cursor.close()
            LOG.log_error(f"Erro recebido ao realizar a query: {e}")
        return results
