import mysql.connector
class capacity:
    def __init__(self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Khan@1997",
        database = "RAILWAY_DMS"
        )
    def capacityinsert(self,trn,ac1,ac2,ac3,sl,gen):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRAIN_CAPACITY VALUES({trn},{ac1},{ac2},{ac3},{sl},{gen})")
        self.conn.commit()
        print("Data has been inserted sucessfully")