import pyodbc
import pymongo

#servername = getenv("TEST_SERVER")
#username = getenv("TEST_USERNAME")
#password = getenv("TEST_PASSWORD")

# h t t p s : / / github .com /mkleehammer/pyodbc/wiki/Getting-started
servername = 'HIPERDRIVE2\MSSQLSERVER01'
port='1433'
database = 'pymssql'
username = 'pymssql'
password = 'pymssql'
driver= '{ODBC Driver 17 for SQL Server}'
connSql = pyodbc.connect(
 ';DRIVER='+driver
+';SERVER='+servername
+';PORT='+port
+';DATABASE='+database
+';UID='+username
+';PWD='+ password
+';Trusted_Connection=yes'
)
cursorSql = connSql.cursor()

print(pymongo.version)
print(pymongo.has_c())
connMongo = pymongo.MongoClient("mongodb://localhost:27017") # connect to the db on standard port
print(connMongo)
dbMongo = connMongo.pymongo # attach to db m101
print(dbMongo)
collMongo = dbMongo.ColecaoUm # specify the collection funnynumbers
print(collMongo)

cursorSql.execute("""
SELECT * FROM dbo.Table_1 WHERE name=?
""",
'pateta'
)
rowSql = cursorSql.fetchone()
descriptionSql = cursorSql.description
print(descriptionSql)
columnNamesSQL = [column[0] for column in cursorSql.description] # h t t p s :// github.com/mkleehammer/pyodbc/issues/171
print(columnNamesSQL)
while rowSql:

    print("Name=%s, bithDate=%s" % (rowSql[0], rowSql[1]))
    print(rowSql)
    try:
        dict4Mongo = dict(zip(columnNamesSQL, rowSql))
        print(dict4Mongo)
        dbMongo.ColecaoUm.insert_one(dict4Mongo)

    except Exception as e:
        print("Error trying to read collection:", type(e), e)

    rowSql = cursorSql.fetchone()

connMongo.close()
connSql.close()
 