import mysql.connector

class DBhelper:

    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user="root",
                password="",
                database='demo-1'
            )
            self.cursor = self.conn.cursor()
            print("Connected to database successfully")
        except Exception as e:
            print("Error connecting to database :", e)
               
    def register_user(self, name, password, grade):
            try:
                self.cursor.execute("""
    INSERT INTO users (name, password, grade) VALUES (%s, %s, %s)
    """, (name, password, grade))
                self.conn.commit()
                return True
            except Exception as e:
                print("Error during registration:", e)
                return False
    
    def search_user(self, name, password):
        try:
            self.cursor.execute("""
SELECT * FROM users WHERE name = %s AND password = %s
""", (name, password))
            result = self.cursor.fetchone() #fetchall()
            return result
        except Exception as e:
            print("Error during user search:", e)
            return None
