import pyodbc

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=mysqlserver-carlos.database.windows.net;"
            "Database=banco_casa;"
            "UID=app_olhos;"
            "PWD=m9Ph!R8i3ySFjqb;")
cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()