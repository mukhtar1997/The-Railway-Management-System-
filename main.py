# importing Required modules
from traindetails import details
from traincapacity import capacity
from routes import routes
from bookin import book
import numpy as np


print("---------Welcome to Railway Management Syestem---------")
print('-------For Inserting the Data Enter - 1--')
print('-------For Reading the Data Enter - 2--')
print('-------For Updating the Data Enter - 3--')
print('-------For Deleting the Data Enter - 4--')

opr = int(input("Please Enter your operation: "))
if opr == 1:
    print('--- For inserting the data in traindetails press 1----')
    print('--- For inserting the data in traincapacity press 2----')
    print('--- For inserting the data in routes press 3----')
    print('--- For booking a ticket press 4----')
    inopr = int(input("Please Select an Operation: "))
    if inopr==1:
        obj = details()
        tno = int(input("please enter train no:"))
        src = input("please enter source station:")
        dist = input("please enter Destination station:")
        tname = input("please enter train name:")
        obj.insertdetails(tno,src,dist,tname)

    if inopr==2:
        obj = capacity()
        obj1 = details()
        obj1.trainofetch()
        trn = int(input("Please Enter train number: "))
        ac1 = int(input("Please Enter Capacity of AC 1: "))
        ac2 = int(input("Please Enter Capacity of AC 2: "))
        ac3 = int(input("Please Enter Capacity of AC 3: "))
        sl = int(input("Please Enter Capacity of Sleeper Class: "))
        gen = int(input("Please Enter Capacity of General Class: "))
        obj.capacityinsert(trn,ac1,ac2,ac3,sl,gen)
    if inopr==3:
        obj = routes()
        obj1 = details()
        obj1.trainofetchroutes()
        trn = int(input("Please Enter train number: "))
        st1 = input("Please Enter stop 1: ")
        st2 = input("Please Enter stop 2: ")
        st3 = input("Please Enter stop 3: ")
        st4 = input("Please Enter stop 4: ")
        obj.routesinsert(trn,st1,st2,st3,st4)
    if inopr==4:
        source = input("From: ")
        dest = input("To: ")
        obj = book()
        obj.trainfetch(source,dest)
        trainno = int(input("Please Enter Trainno: "))
        cls = input("Please Enter your Coach: ")
        #passenger info
        pid = int(input("Please Enter Your Id: "))
        pname = input("Please Enter Your Name: ")
        age = int(input("Please Enter Your Age: "))
        gen = input("Please Enter Your Gender: ")
        mn = int(input("Please Enter Your Mobile No: "))
        obj.addpassenger(pid,pname,age,gen,mn)
        # making Transaction
        tid = int(input("Please Enter Your Id: "))
        amount = int(input("Please Enter amount: "))
        mode = input("Please Enter Payment Mode: ")
        obj.addtransaction(tid,pid,amount,mode)
        # Booking ticket
        bid = np.random.randint(0,500000,1)[0]
        stno = np.random.randint(0,50,1)[0]
        obj.bookticket(bid,pid,cls,stno,tid,source,dest,trainno)

if opr == 2:
    pass
if opr == 3:
    pass
if opr == 4:
    pass

























