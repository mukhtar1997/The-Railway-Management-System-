#trying to fetch the data into list means
#suppose in source one city is delhi and destination is hyd
#that means when user select any city so data should be present in data and 
#when user select any city in source and dest

import mysql.connector
class book:
    def __init__(self):
        self.conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Khan@1997",
        database = "RAILWAY_DMS"
        )
    def trainfetch(self,src,dest):
        cur = self.conn.cursor()
        cur.execute(f'''select routes.train_no,source,stop1,stop2,stop3,stop4,destination
                    from routes inner join train_details
                    on routes.train_no=train_details.train_no where source='{src}' or 
                    stop1='{src}' or stop2='{src}' or stop3='{src}' or stop4='{src}';''')
        dt = cur.fetchall()
        try:
            tr = []
            for i in dt:
                for j in i[i.index(src)+1:]:
                    if j==dest:
                        tr.append(i)
        except:
            pass
        print(tr)
    
    def addpassenger(self,pid,pname,age,gen,mn):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO PASSENGERS VALUES({pid},'{pname}',{age},{mn},'{gen}')")
        self.conn.commit()
        print("Data has been inserted sucessfully")
    def addtransaction(self,tid,pid,amount,mode):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO TRANSACTIONS VALUES({tid},{pid},{amount},'{mode}')")
        self.conn.commit()
        print("Transaction sucessfull")
    def bookticket(self,bid,pid,cls,stno,tid,source,dest,trainno):
        self.cur = self.conn.cursor()
        self.cur.execute(f"INSERT INTO BOOK_TICKETS VALUES({bid},{pid},'{cls}',{stno},{tid},'{source}','{dest}',{trainno})")
        self.conn.commit()
        print("Ticket has been booked")   
        print(" This is  Your Passenger Id: ",pid)
        print("This is Your Seat Number: ",stno)
        print("This is Your Booking Id: ",bid)
        print("This is Your Coach Name: ",cls)
        print("This is Your Source Station: ",source)
        print("This is your Destination Station: ",dest)
        print("This is Your Journey Train No: ",trainno)
        print("This is Your Transaction Id: ",tid)
















