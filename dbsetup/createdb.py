#Create initial database
import pymysql
import config as cfg

humanresourcesdb = pymysql.connect(
    host=cfg.mysqldb['host'],
    user=cfg.mysqldb['username'],
    password=cfg.mysqldb['password'],
    database=cfg.mysqldb['database']
) 

cursor = humanresourcesdb.cursor()
createdb = 'CREATE DATABSE humanresourcesdb'
cursor.execute(createdb)

humanresourcesdb.close()
cursor.close()