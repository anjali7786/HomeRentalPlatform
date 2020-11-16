CREATE DATABASE propertymanagement;
USE propertymanagement; 
CREATE TABLE  accounts (
  	  id int(110) NOT NULL AUTO_INCREMENT,
  	  username varchar(50) NOT NULL,
      fullname varchar(50) NOT NULL,
      email varchar(50) NOT NULL,
      mobile varchar(10) NOT NULL,
	  password varchar(255) NOT NULL,
 	  cpassword varchar(255) NOT NULL,
      PRIMARY KEY (id)
); 
CREATE TABLE apartmentdetail (
    A_ID int(110) NOT NULL AUTO_INCREMENT,
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
    Atype varchar(50) NOT NULL,
    RS varchar(4) NOT NULL,
 	Availability varchar(20) NOT NULL,
	Price numeric NOT NULL,
 	Facilities varchar(250) NOT NULL,
 	Dscrption varchar(500) NOT NULL,
 	image varchar(10000) NOT NULL,
    Username varchar(50) NOT NULL,
    PRIMARY KEY (A_ID)
);
CREATE TABLE roomdetail(
 	R_ID int NOT NULL AUTO_INCREMENT,
	Email varchar(100) NOT NULL,
 	Mobile numeric(10) NOT NULL,
 	Room_no varchar(50) NOT NULL,
 	Address varchar(100) NOT NULL,
 	Landmark varchar(100) NOT NULL,
 	City varchar(50) NOT NULL,
 	Pincode decimal(6,0) NOT NULL,
 	State varchar(50) NOT NULL,
 	Country varchar(50) NOT NULL,
 	Availability varchar(20) NOT NULL,
 	Rent numeric NOT NULL,
	Facilities varchar(250) NOT NULL,
 	Dscrption varchar(500) NOT NULL,
    image varchar(10000) NOT NULL,
    Username varchar(50) NOT NULL,
 	PRIMARY KEY (R_ID)
 );
 CREATE TABLE complaints (
C_ID int NOT NULL AUTO_INCREMENT,
A_ID int NOT NULL,
Aname varchar(50) NOT NULL,
Complaint varchar(250) NOT NULL,
Flag int(1) DEFAULT 0,
PRIMARY KEY (C_ID),
FOREIGN KEY (A_ID) REFERENCES apartmentdetail(A_ID) ON DELETE CASCADE
); 
CREATE TABLE complaints2 (
C_ID int NOT NULL AUTO_INCREMENT,
R_ID int NOT NULL,
Room_no varchar(50) NOT NULL,
Complaint varchar(250) NOT NULL,
Flag int(1) DEFAULT 0,
PRIMARY KEY (C_ID),
FOREIGN KEY (R_ID) REFERENCES roomdetail(R_ID) ON DELETE CASCADE
);
CREATE TABLE Buy_propertyapt(
    bapt_id int(110) NOT NULL AUTO_INCREMENT,
    A_ID int(110) NOT NULL,
    Aname varchar(50) NOT NULL,
    Fullname varchar(50) NOT NULL,
    Email varchar(100) NOT NULL,
    Mobile decimal(10,0) NOT NULL,
    Age int NOT NULL,
    Address varchar(100) NOT NULL,
    Landmark varchar(100) NOT NULL,
    City varchar(50) NOT NULL,
    Pincode decimal(6,0) NOT NULL,
    State varchar(50) NOT NULL,
    Occupation varchar(50) NOT NULL,
    Username varchar(50) NOT NULL,
    Applicant varchar(50) NOT NULL,
    Status varchar(50) NOT NULL,
    primary key(bapt_id),
    foreign key(A_ID) references apartmentdetail(A_ID) ON DELETE CASCADE
);
CREATE TABLE Buy_propertyroom(
    bapt_id int(110) NOT NULL AUTO_INCREMENT,
    R_ID int(110) NOT NULL,
    Room_no varchar(50) NOT NULL,
    Fullname varchar(50) NOT NULL,
    Email varchar(100) NOT NULL,
    Mobile decimal(10,0) NOT NULL,
    Age int NOT NULL,
    Address varchar(100) NOT NULL,
    Landmark varchar(100) NOT NULL,
    City varchar(50) NOT NULL,
    Pincode decimal(6,0) NOT NULL,
    State varchar(50) NOT NULL,
    Occupation varchar(50) NOT NULL,
    Username varchar(50) NOT NULL,
    Applicant varchar(50) NOT NULL,
	Status varchar(50) NOT NULL,
    primary key(bapt_id),
    foreign key(R_ID) references roomdetail(R_ID) ON DELETE CASCADE
);
CREATE TABLE approved (
X_ID int NOT NULL AUTO_INCREMENT,
Aname varchar(50) NOT NULL,
Applicant varchar(50) NOT NULL,
email varchar(50) NOT NULL,
mobile varchar(10) NOT NULL,
PRIMARY KEY (X_ID)
);
CREATE TABLE approved2 (
X_ID int NOT NULL AUTO_INCREMENT,
Room_no varchar(50) NOT NULL,
Applicant varchar(50) NOT NULL,
email varchar(50) NOT NULL,
mobile varchar(10) NOT NULL,
PRIMARY KEY (X_ID)
);
INSERT INTO accounts (id, username, fullname,email,mobile,password,cpassword) VALUES (1, 'admin', 'admin','admin@gmail.com','1234567890','$2b$12$27a0Gq6GPpr6IT.ANU4RS.lpb9avi5FlPC0PWgk9JaW8r0on830ka','$2b$12$27a0Gq6GPpr6IT.ANU4RS.lpb9avi5FlPC0PWgk9JaW8r0on830ka');
Select * from accounts;
