CREATE DATABASE propertymanagement;

USE propertymanagement;


CREATE TABLE  accounts (
	id int(11) NOT NULL AUTO_INCREMENT,
  	username varchar(50) NOT NULL,
    fullname varchar(50) NOT NULL,
    email varchar(50) NOT NULL,
    mobile varchar(10) NOT NULL,
  	password varchar(255) NOT NULL,
    cpassword varchar(255) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE apartmentdetail (
  A_ID int NOT NULL AUTO_INCREMENT,
  Aname varchar(50) NOT NULL,
  Email varchar(100) NOT NULL,
  Mobile decimal(10,0) NOT NULL,
  Plot_no int NOT NULL,
  Address varchar(100) NOT NULL,
  Landmark varchar(100) NOT NULL,
  City varchar(50) NOT NULL,
  Pincode decimal(6,0) NOT NULL,
  State varchar(50) NOT NULL,
  Country varchar(50) NOT NULL,
  PRIMARY KEY (A_ID)
)


INSERT INTO accounts (id, username, fullname,email,mobile,password,cpassword) VALUES (1, 'admin', 'admin','admin@gmail.com','1234567890','admin','admin');

select * from accounts;
  
  

