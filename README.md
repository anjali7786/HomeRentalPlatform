# HomeRentalPlatform
  This portal is designed to provide the facility where a customer can easily buy or sell their properties such as apartment & room. The user can be both buyer or seller. The user just has to register on this web portal, then the user can easily upload information of their properties to sell and also search for properties to buy. The system contains a search filter which helps users to search property in a certain city, state or according to the price range. Users can also make complaints against apartment/rooms. But the owner cannot buy/make complaints for his/her own property. The owner can edit/delete his/her property details whenever they want. Seller can approve multiple buyers for his property. Users also receives notifications when someone make complaints against his property or when someone applies for his property. Buyer will also receive notification if his application has been approved. The admin can see list of registered users, details of properties and controls the complaints and if he founds that the complaint is correct he sends the warning notification to the respective owner.

INSTRUCTIONS FOR PROJECT SETUP

Step1:
You can directly download the zip file or follow next 2 steps to clone the repo.
Install latest version of git. Open the above github repository link in browser. Click on the code button as shown in the figure and copy the marked https url 
Step2:
Create new folder and open git bash inside that folder write command- 
git clone https://github.com/anjali7786/HomeRentalPlatform.git
Step3:
•	Install latest version of python and a code editor (Pycharm or Visual Studio Code).
•	Installing required packages by writing following commands on command prompt:
•	pip install flask
•	Download & Install MYSQLCLIENT For Python : https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient open this link and under MySQLclient select the wheel according to your python version and 32/64 bit windows system.
•	After installing the wheel Open command prompt inside that folder.
To open a command prompt window in any folder, simply hold down the Shift key and right-click on the desktop. In the context menu, you will see the option to Open command window here. Clicking on it will open a CMD window.
And write the below command in cmd.
•	pip install flask-mysqldb
•	pip install bcrypt
Step4:
Create a local host connection and click on Server Tab then select Data Import. You can see that there are two options import from self-contained file and import from dump project folder choose the option import from self-contained file and browse to the location where the propertymanagement.sql file is present and click on start import which is on the bottom right of this window.  Then go to the schemas tab and click on refresh to see the new database named propertymanagement added. The database setup is completed. 
Step5:
Open the project files in the code editor. Open main.py file and if your MySQL username and password are not “root” then you can replace the username and password written in main.py file with your MySQL username and password. Now run the main.py file and click on the localhost link of the project.
 Go to http://127.0.0.1:5000/ to see the project.
