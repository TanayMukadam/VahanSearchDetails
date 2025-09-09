import pymysql
from fastapi import HTTPException, status
import os
from dotenv import load_dotenv


load_dotenv()



class Database:
    
    
    def __init__(self):
        self.host = os.environ.get("DATABASE_HOST")
        self.username = os.environ.get("DATABASE_USER")
        self.password = os.environ.get("DATABASE_PASS")
        self.database = os.environ.get("DATABASE_NAME")
        self.connection = None
        
        
        
    def connect_db(self):
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.database)
            print("Database Connected Successfully")
            
            self.connection = connection
            return self.connection
        except Exception as e:
            print(f"Database Connection Failed: {e}")
            raise e
        
        
    def get_result(self, reg_no, phone_no):
        
        self.connect_db()
        result = None
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        
        
        if reg_no:
            cursor.callproc("sp_get_vehicle_by_regNo", (reg_no,))
            result = cursor.fetchall()
        elif phone_no:
            cursor.callproc("sp_get_vehicle_by_mobile", (phone_no,))
            result = cursor.fetchall()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Registration Number or Phone Number Found")
        
        return result
    
    
    def create_user(self, username, password):
        self.connect_db()
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO users (username, password) VALUES (%s, %s)"

        try:
            cursor.execute(insert_query, (username, password))
            self.connection.commit()
            
            return {"status": "Successfull", "message": "User Created"}
        except pymysql.err.IntegrityError as e:
            # Handle unique constraint violation (e.g. duplicate username)
            self.connection.rollback()
            print(f"Create User Failed: {e}")
            raise HTTPException(status_code=400, detail="Username already exists")
        finally:
            cursor.close()
            self.connection.close()
            
            
    
    def get_user(self, username: str):
        self.connect_db()
        cursor = self.connection.cursor(pymysql.cursors.DictCursor)  # Get dict results
        
        query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        
        cursor.close()
        self.connection.close()
        
        return user
    
    
    def log_search(self, username, regno=None, phoneno=None):
        self.connect_db()
        cursor = self.connection.cursor()
        sql = """
        INSERT INTO search_logs (username, regno, phoneno)
        VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (username, regno, phoneno))
        self.connection.commit()
        cursor.close()


