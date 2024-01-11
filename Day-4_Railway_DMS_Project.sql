CREATE DATABASE RAILWAY_DMS;
USE RAILWAY_DMS;

create table passengers
(
P_ID INT PRIMARY KEY,
P_NAME VARCHAR(30),
AGE INT ,
MO_NUM INT , 
GENDER VARCHAR(30)
);

CREATE TABLE TRAIN_DETAILS
(
TRAIN_NO INT PRIMARY KEY ,
SOURCE VARCHAR(30),
DESTINATION VARCHAR(30),
TRAIN_NAME VARCHAR(30)
);

CREATE TABLE TRANSACTIONS
(
T_ID INT PRIMARY KEY ,
P_ID INT,
FARE INT,
PAYMENT_MODE VARCHAR(30),
FOREIGN KEY(P_ID) REFERENCES passengers(P_ID)
);

CREATE TABLE TRAIN_CAPACITY
(
TRAIN_NO INT PRIMARY KEY ,
AC_1 INT,
AC_2 INT,
AC_3 INT,
SL INT,
GENERAL int,
FOREIGN KEY(TRAIN_NO) references TRAIN_DETAILS (TRAIN_NO)
);

CREATE TABLE ROUTES
(
TRAIN_NO INT PRIMARY KEY,
STOP1 VARCHAR(30),
STOP2 VARCHAR(30),
STOP3 VARCHAR(30),
STOP4 VARCHAR(30),
foreign key(TRAIN_NO) references TRAIN_DETAILS(TRAIN_NO)
);


CREATE TABLE BOOK_TICKETS
(
BOOKING_ID INT PRIMARY KEY,
P_ID INT,
CLASS VARCHAR(30),
SEAT_NO INT ,
T_ID INT ,
SOURCE VARCHAR(30),
DESTINATION VARCHAR(30),
TRAIN_NO INT,
FOREIGN KEY(P_ID) REFERENCES PASSENGERS(P_ID),
FOREIGN KEY(T_ID) REFERENCES TRANSACTIONS(T_ID),
FOREIGN KEY(TRAIN_NO) REFERENCES TRAIN_DETAILS(TRAIN_NO)
);

SHOW TABLES;
SELECT*FROM TRAIN_CAPACITY;

USE RAILWAY_DMS;

SELECT train_details.train_no from train_details
left join train_capacity
on train_details.train_no=train_capacity.train_no
where ac_1 is null;

select*from routes;
select*from train_details;

update routes
set stop1='hydd'
where stop1='hyd';

set sql_safe_updates=0;

update routes set stop1 = "hyd", stop2 = "ngp", stop3 = "bhp",stop4="agr"
where Train_no = 14527;

select routes.train_no,source,stop1,stop2,stop3,stop4,destination
from routes inner join train_details
on routes.train_no=train_details.train_no where source="bhp" or 
stop1="bhp" or stop2="bhp" or stop3="bhp" or stop4="bhp";


insert into routes 




















