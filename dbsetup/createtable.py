# create tables
import pymysql
import config as cfg

humanresourcesdb = pymysql.connect(
    host=cfg.mysqldb['host'],
    user=cfg.mysqldb['username'],
    password=cfg.mysqldb['password'],
    database=cfg.mysqldb['database']
) 

cursor = humanresourcesdb.cursor()

#employees table
employeeTable='''CREATE TABLE employees (
StaffID INT AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(250),
Position VARCHAR(250),
Role VARCHAR(250),
DepartmentID INT,

) '''
cursor.execute(employeeTable)

#departments table
departmentTable='''CREATE TABLE departments (
DepartmentID INT,
DepartmentName VARCHAR(250),

)'''

cursor.execute(departmentTable)

humanresourcesdb.close()
cursor.close()