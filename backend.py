import mysql.connector

class Code():
    def __init__(self) -> None:
        self.usedDatabase()
        self.createTable()

    def usedDatabase(self):
        try:    
            self.conn = mysql.connector.connect(
                host = 'localhost',
                database = 'universitydb',
                user = 'root',
                password = 'root'
            )
        except Exception as err:
            print(err)
        else:
            print('Databazaga ulandi') 

    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql = 'create table if not exists user (id serial, product varchar(12) not null unique, price int not null, amount int not null)'
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            print('Table yaratildi') 
               
    def addProduct(self,product,price,amount):
        try:
            with self.conn.cursor() as cursor:
                sql = f"insert into user (product,price,amount) values ('{product}','{price}','{amount}')"   
                cursor.execute(sql)
        except Exception as err:
            print( err)
        else:
            self.conn.commit()
            print('ok')
            

    def deleteProduct(self,product):    
        try:
            with self.conn.cursor() as cursor:
                sql = f"delete from user where product = '{product}'"   
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            print('deleted') 

    def getAll(self):
        try:
            with self.conn.cursor() as cursor:
                sql = "select * from user"   
                cursor.execute(sql)
                res  = cursor.fetchall()
        except Exception as err:
            print(err)
        else:

            return res 

    def searcProduct(self,product):
        try:
            with self.conn.cursor() as cursor:
                sql = f"select * from user where product ='{product}'"   
                cursor.execute(sql)
                res = cursor.fetchall()
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            return res                                      
                         
c = Code()
c.getAll()
#by shohnur
 

   
   
  
            
