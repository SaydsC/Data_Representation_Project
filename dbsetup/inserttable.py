# insert into tables
import pymysql
import config as cfg

humanresourcesdb = pymysql.connect(
    host=cfg.mysqldb['host'],
    user=cfg.mysqldb['username'],
    password=cfg.mysqldb['password'],
    database=cfg.mysqldb['database']
) 

cursor = humanresourcesdb.cursor()

sqlinsert="insert into Employees (Name, Position, Role, DepartmentID) VALUES (%s,%s,%s,%s)"

values = ['John Smith', 'Senior Management', 'HR Business Partner', 101]
        
cursor.execute(sqlinsert, values)
humanresourcesdb.commit()
print('employee added to employee database')

humanresourcesdb.close()
cursor.close()
