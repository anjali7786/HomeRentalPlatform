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

INSERT INTO accounts (id, username, fullname,email,mobile,password,cpassword) VALUES (1, 'admin', 'admin','admin@gmail.com','1234567890','admin','admin');
select * from accounts;