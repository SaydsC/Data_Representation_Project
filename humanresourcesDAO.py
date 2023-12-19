import mysql.connector
class humanresourcesDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self): 
        #these should be read from a config file
        self.host="localhost"
        self.user="root"
        self.password=""
        self.database="humanresourcesdb"
               
    
    def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    def closeAll(self):
        self.connection.close()
        self.cursor.close()
    
    def create(self, values):
        cursor = self.getCursor()
        sql="insert into Employees (Name, Position, Role, DepartmentID) values (%s,%s,%s,%s)"
        cursor.execute(sql, values)

        self.connection.commit()
        newStaffID = cursor.lastrowid
        self.closeAll()
        return newStaffID

    def getAll(self):
        cursor = self.getCursor()
        sql="select * from Employees"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findByStaffID(self, StaffID):
        cursor = self.getCursor()
        sql="select * from Employees where StaffID = %s"
        values = (StaffID,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    def update(self, values):
        cursor = self.getCursor()
        sql="update Employees set Name= %s, Position=%s, Role=%s, DepartmentID=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    def delete(self, StaffID):
        cursor = self.getCursor()
        sql="delete from Employees where StaffID = %s"
        values = (StaffID,)

        cursor.execute(sql, values)

        self.connection.commit()
        self.closeAll
        #print("delete done")

humanresourcesDAO = humanresourcesDAO()