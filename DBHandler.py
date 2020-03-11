import psycopg2



class DBHandler:
    def __init__(self,DATABASEIP,DB_USER,DB_PASSWORD,DATABASE ):
        self.DATABASEIP = DATABASEIP
        self.DATABASE = DATABASE
        self.DB_USER = DB_USER
        self.DB_PASSWORD = DB_PASSWORD

    def  __del__(self):
        print("Destructor")


    def signin(self,email,password):
        db = None
        cursor = None
        insert = False
        try:
            db =psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE,user=self.DB_USER, password=self.DB_PASSWORD,)
            cur = db.cursor()
            print("here")
            sql =  "SELECT fname ,lname,wins,lost  FROM players WHERE email = %s AND password = %s"
            args = (email,password)
            cur.execute(sql,(email,password,))
            result=cur.fetchone()
            print(result)
            if(result!= None):
                return result[0]
            else:
                return None

        except Exception as e:
            print(e)
            print("some error")


    def isAlreadyTaken(self,email):
        db = None
        cursor = None
        insert = False
        result=None
        try:
            db = psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE, user=self.DB_USER,password=self.DB_PASSWORD, )
            cur = db.cursor()
            print("here")
            sql =  "SELECT * FROM players WHERE email = %s "
            args = (email)
            cur.execute(sql,(email,))
            result=cur.fetchone()
            print(result)
            if(result== None):
                return True
            else:
                return False

        except Exception as e:
            print(e)
            print("some error")




    def existPass(self,password):
        db = None
        cursor = None
        insert = False
        result=None
        try:
            db = psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE, user=self.DB_USER,password=self.DB_PASSWORD, )
            cur = db.cursor()
            print("here")
            sql =  "SELECT * FROM players WHERE password = %s "
            args = (password)
            cur.execute(sql,(password,))
            result=cur.fetchone()
            print(result)
            if(result== None):
                return False
            else:
                return True

        except Exception as e:
            print(e)
            print("some error")



    def winlose(self,winner,loser1,loser2,loser3):
        db = None
        cursor = None
        insert = False
        result=None
        try:
            db =psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE,user=self.DB_USER, password=self.DB_PASSWORD,)
            cur = db.cursor()
            print("here")
            sql="Select wins from players where email=%s"
            args = (winner)
            cur.execute(sql,(winner,))
            result=cur.fetchone()
            result=result+1
            sql1 = "Update players SET wins=%s  WHERE email = %s"
            args = (result,winner)
            cur.execute(sql1, (result,winner,))
            sql2 = "Select lost from players where email=%s"
            args=(loser1)
            cur.execute(sql2, (loser1,))
            result = cur.fetchone()
            result=result+1
            sql3 = "Update players SET lost=%s  WHERE email = %s"
            args = (result, loser1)
            cur.execute(sql3,(result, loser1,))

            args = (loser2)
            cur.execute(sql2,(loser2,))
            result = cur.fetchone()
            result = result + 1
            args = (result, loser2)
            cur.execute(sql3, args)

            args = (loser3)
            cur.execute(sql2, (loser3,))
            result = cur.fetchone()
            result = result + 1
            args = (result, loser3)
            cur.execute(sql3, (result, loser3,))

        except Exception as e:
            print(e)
            print("some error")

    def getWins(self,email):
        db = None
        cursor = None
        insert = False
        result = None
        try:
            db =psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE,user=self.DB_USER, password=self.DB_PASSWORD,)
            cur = db.cursor()
            print("here")
            sql = """Select wins from players where email=%s;"""
            args = (email)
            cur.execute(sql, (email,))
            result = cur.fetchone()
            return result[0];
        except Exception as e:
            print(e)
            print("some error")

    def getLoses(self,email):
        db = None
        cursor = None
        insert = False
        result = None
        try:
            db =psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE,user=self.DB_USER, password=self.DB_PASSWORD,)
            cur = db.cursor()
            print("here")
            sql = """Select lost from players where email=%s;"""
            args = (email)
            cur.execute(sql, (email,))
            result = cur.fetchone()
            return result[0];
        except Exception as e:
            print(e)
            print("some error")


    def signup(self,email,password,fname,lname):
        db = None
        cursor = None
        insert = False
        try:
            db =psycopg2.connect(host=self.DATABASEIP, database=self.DATABASE,user=self.DB_USER, password=self.DB_PASSWORD,)
            cur = db.cursor()
            print("here")
            sql = """INSERT INTO players (fname,lname,email,password) VALUES (%s,%s,%s,%s);"""
            args = (fname, lname,email, password)
            cur.execute(sql, (fname, lname,email, password,))
            insert= True

        except Exception as e:
            print(e)
            print("some error")
        finally:
            if(db!=None):
                db.commit()
                db.commit()
            return insert




def Test():
    db = DBHandler("localhost", "root", "123","test")
    mylist = db.showUsers("test")
    for i in mylist:
        print(i)
if __name__ == '__main__':
    Test()





