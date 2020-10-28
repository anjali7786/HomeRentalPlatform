from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os,uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = '66710c44ea2f24084dd73f9a'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'propertymanagement'

mysql = MySQL(app)

@app.route("/",methods =['GET', 'POST'])
def home():
    msg=""
    op=""
    if request.method == 'POST':
        loc = request.form['location']
        city = request.form['city']
        option = request.form['options']
        minprice = request.form['minprice']
        maxprice = request.form['maxprice']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if option=="apartments":
            op="a"
            if loc=="" and city=="" and minprice=="" and maxprice=="":
                cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail')
                result = cur.fetchall()
            elif loc!="":
                if city=="" and minprice=="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s',[loc])
                    result = cur.fetchall()
                elif city!="" and minprice=="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and City = %s',([loc],[city]))
                    result = cur.fetchall()
                elif city!="" and minprice!="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and City = %s and Price>=%s',([loc], [city],[minprice]))
                    result = cur.fetchall()
                elif city!="" and minprice=="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and City = %s and Price<=%s',([loc], [city],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice=="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and Price<=%s',([loc],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice!="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and Price<=%s',([loc],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice!="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and Price>=%s and Price<=%s',([loc], [minprice],[maxprice]))
                    result = cur.fetchall()
                elif city!="" and minprice!="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where State = % s and City=%s and Price>=%s and Price<=%s',([loc],[city], [minprice],[maxprice]))
                    result = cur.fetchall()
            elif city!="" and loc=="":
                if minprice=="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where City = % s',[city])
                    result = cur.fetchall()
                elif minprice=="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where City = % s and Price<=%s',([city],[maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where City = % s and Price<=%s',([city],[maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where City = % s and Price>=%s and Price<=%s',([city], [minprice],[maxprice]))
                    result = cur.fetchall()
            elif city=="" and loc=="":
                if minprice=="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where Price<=%s',([maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice=="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where Price>=%s',([minprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice!="":
                    cur.execute('SELECT A_ID,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Descrption,image FROM apartmentdetail where Price>=%s and Price<=%s',([minprice],[maxprice]))
                    result = cur.fetchall()
        elif option=="rooms":
            op="r"
            if loc=="" and city=="" and minprice=="" and maxprice=="":
                cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail')
                result = cur.fetchall()
            elif loc!="":
                if city=="" and minprice=="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s',[loc])
                    result = cur.fetchall()
                elif city!="" and minprice=="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and City = %s',([loc],[city]))
                    result = cur.fetchall()
                elif city!="" and minprice!="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and City = %s and Rent>=%s',([loc], [city],[minprice]))
                    result = cur.fetchall()
                elif city!="" and minprice=="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and City = %s and Rent<=%s',([loc], [city],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice=="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and Rent<=%s',([loc],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice!="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and Rent<=%s',([loc],[maxprice]))
                    result = cur.fetchall()
                elif city=="" and minprice!="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and Rent>=%s and Rent<=%s',([loc], [minprice],[maxprice]))
                    result = cur.fetchall()
                elif city!="" and minprice!="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where State = % s and City=%s and Rent>=%s and Rent<=%s',([loc],[city], [minprice],[maxprice]))
                    result = cur.fetchall()
            elif city!="" and loc=="":
                if minprice=="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where City = % s',[city])
                    result = cur.fetchall()
                elif minprice=="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where City = % s and Rent<=%s',([city],[maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where City = % s and Rent<=%s',([city],[maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where City = % s and Rent>=%s and Price<=%s',([city], [minprice],[maxprice]))
                    result = cur.fetchall()
            elif city=="" and loc=="":
                if minprice=="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where Rent<=%s',([maxprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice=="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where Rent>=%s',([minprice]))
                    result = cur.fetchall()
                elif minprice!="" and maxprice!="":
                    cur.execute('SELECT R_ID,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Descrption,image,Rent FROM roomdetail where Rent>=%s and Rent<=%s',([minprice],[maxprice]))
                    result = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        if result:
            if 'loggedin' in session:
               return render_template('index.html', detail=result,msg="Result for the search",op=op,username=session['username'])
            else:
                return render_template('index.html', detail=result, msg="Result for the search", op=op,username="")
        else:
            if 'loggedin' in session:
                return render_template('index.html', detail="No records found",username=session['username'])
            else:
                return render_template('index.html', detail="No records found",username="" )
    else:
        if 'loggedin' in session:
           return render_template('index.html',username=session['username'])
        else:
            return render_template('index.html', username="")


@app.route("/about")
def about():
    if 'loggedin' in session:
        return render_template('about.html',username=session['username'])
    else:
        return render_template('about.html', username="")

@app.route("/login/", methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username) > 0 and len(password) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
            account = cursor.fetchone()
            mysql.connection.commit()
            cursor.close()
            if account:
                if username == 'admin' and password == 'admin':
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    session['email1'] = account['email']
                    return redirect(url_for('dashboard'))
                else:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    session['email1'] = account['email']
                    return redirect(url_for('userdashboard'))
            else:
                msg = 'Incorrect username/password!'
        else:
            msg = ' Please fill the entries !'
    return render_template('login.html', msg=msg)


@app.route('/login/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    session.pop('email1', None)
    return redirect(url_for('login'))


@app.route("/register/", methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']
        email = request.form['email']
        mobile = request.form['mobile']
        cpassword = request.form['cpassword']
        if len(username) > 0 and len(password) > 0 and len(email) > 0 and len(mobile) > 0 and len(fullname) > 0 and len(
                cpassword) > 0:
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM accounts WHERE username = % s', (username,))
            account = cursor.fetchone()
            cursor.execute('SELECT * FROM accounts WHERE email = % s', (email,))
            account1 = cursor.fetchone()
            cursor.execute('SELECT * FROM accounts WHERE mobile = % s', (mobile,))
            account2 = cursor.fetchone()
            if account:
                msg = 'Account already exists with this username!'
            elif account1:
                msg = 'Account already exists with this email !'
            elif account2:
                msg = 'Account already exists with this mobile number !'
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
            elif not re.match(r'[A-Za-z0-9]+', username):
                msg = 'Username must contain only characters and numbers !'
            elif not username or not password or not email or not mobile or not cpassword or not fullname:
                msg = 'Please fill out the form !'
            elif len(mobile) != 10:
                msg = 'Enter 10 digit number !'
            elif cpassword != password:
                msg = 'Confirm password does not match with password !'
            else:
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s,% s,% s,% s)',
                               (username, fullname, email, mobile, password, cpassword,))
                mysql.connection.commit()
                cursor.close()
                msg = 'You have successfully registered !'
        else:
            msg = 'Please fill out the form !'

    return render_template('register.html', msg=msg)


@app.route("/dashboard/")
def dashboard():
    if 'loggedin' in session:
        # return render_template('dashboard.html', username=session['username'])
        return render_template('dashboard.html', username='admin', email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/userdashboard/")
def userdashboard():
    if 'loggedin' in session:
        return render_template('userdashboard.html', username=session['username'], email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/registeredusers/")
def registeredusers():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM accounts")
        if resultValue > 0:
            userDetails = cur.fetchall()
            return render_template('registeredusers.html', userDetails=userDetails, username=session['username'], email1=session['email1'])


@app.route('/userdashboard/apmt_reg/', methods=['GET', 'POST'])
def apmt_reg():
    msg = ''
    if request.method == 'POST':
        # fetch data
        details = request.form
        apmtname = details['name']
        email = details['Email']
        mobile = details['Mobile']
        plot_no = details['Plot']
        address = details['Address']
        landmark = details['Landmark']
        city = details['City']
        pin = details['Pincode']
        state = details['State']
        country = details['Country']
        atype = details['Atype']
        rs = details['Rent/Sale']
        availability = details['status']
        Price = details['Price']
        facilities = details['Facilities']
        description = details['Description']
        file = request.files['file']
        extension = os.path.splitext(file.filename)
        f_name = str(uuid.uuid4()) + str(extension)
        app.config['UPLOAD_FOLDER'] = 'static/Uploads'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO apartmentdetail VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (apmtname, email, mobile, plot_no, address, landmark, city, pin, state, country, atype, rs, availability,Price,facilities,description,file))
        mysql.connection.commit()
        cur.close()
        # msg = 'Registration Successful! Thank You !'
    return render_template('Apmt_reg.html', username=session['username'], email1=session['email1'])


@app.route('/userdashboard/room_reg/', methods=['GET', 'POST'])
def room_reg():
    msg = ''
    if request.method == 'POST':
        # fetch data
        details = request.form
        email = details['Email']
        mobile = details['Mobile']
        plot_no = details['Plot']
        address = details['Address']
        landmark = details['Landmark']
        city = details['City']
        pin = details['Pincode']
        state = details['State']
        country = details['Country']
        availability = details['status']
        rent = details['Rent']
        facilities = details['Facilities']
        description = details['Description']
        file = request.files['file']
        extension = os.path.splitext(file.filename)
        f_name = str(uuid.uuid4()) + str(extension)
        app.config['UPLOAD_FOLDER'] = 'static/Uploads'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO roomdetail VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (email, mobile, plot_no, address, landmark, city, pin, state, country, availability, rent, facilities, description, file))
        mysql.connection.commit()
        cur.close()
        # msg = 'Registration Successful! Thank You !'
    return render_template('roomreg.html', username=session['username'],  email1=session['email1'])

@app.route('/complaints/<string:id>', methods=['GET', 'POST'])
def complaints(id):
    msg = ''
    if request.method == 'POST':
        # fetch data
        data = request.form
        A_ID = data['A_ID']
        apmtname = data['name']
        complaint = data['complaint']
        if len(A_ID) > 0 and len(apmtname) > 0 and len(complaint) > 0 :
             cur = mysql.connection.cursor()
             cur.execute("INSERT INTO complaints VALUES(NULL, %s, %s, %s)",
                        (A_ID,apmtname, complaint))
             mysql.connection.commit()
             cur.close()
             msg = '   A complaint has been successfully registered'
             return render_template('complaints.html',msg=msg,id=id,username=session['username'],email1=session['email1'])
        else:
            msg = '   Please fill out the form !'

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT Aname from apartmentdetail where A_ID=%s', [id,])
    data = cursor.fetchall()
    cursor.close()
    return render_template("complaints.html",datas=data,msg=msg,id=id,username=session['username'])

@app.route('/complaints2/<string:id>', methods=['GET', 'POST'])
def complaints2(id):
    msg = ''
    if request.method == 'POST':
        # fetch data
        data = request.form
        R_ID = data['R_ID']
        complaint = data['complaint']
        if len(R_ID) > 0 and len(complaint) > 0 :
             cur = mysql.connection.cursor()
             cur.execute("INSERT INTO complaints2 VALUES(NULL, %s, %s)",
                        (R_ID, complaint))
             mysql.connection.commit()
             cur.close()
             msg = '   A complaint has been successfully registered'
             return render_template('complaints2.html',msg=msg,id=id,username=session['username'])
        else:
            msg = '   Please fill out the form !'

    return render_template("complaints2.html",msg=msg,id=id,username=session['username'])

@app.route('/editapart/<string:id>', methods=['GET', 'POST'])
def editapart(id):
    msg = ''
    if request.method == 'POST':
        # fetch data
        details = request.form
        apmtname = details['name']
        email = details['Email']
        mobile = details['Mobile']
        plot_no = details['Plot']
        address = details['Address']
        landmark = details['Landmark']
        city = details['City']
        pin = details['Pincode']
        state = details['State']
        country = details['Country']
        atype = details['Atype']
        rs = details['Rent/Sale']
        availability = details['status']
        Price = details['Price']
        facilities = details['Facilities']
        description = details['Description']
        file = request.files['file']
        extension = os.path.splitext(file.filename)
        f_name = str(uuid.uuid4()) + str(extension)
        app.config['UPLOAD_FOLDER'] = 'static/Uploads'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        if len(apmtname) > 0 and len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(atype) > 0 and len(facilities) > 0:
             cur = mysql.connection.cursor()
             cur.execute("UPDATE apartmentdetail SET Aname=%s, Email =%s, Mobile =%s, Plot_no=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Atype=%s,RS=%s, Availability=%s,Price=%s,Facilities=%s,Descrption=%s,image=%s WHERE A_ID=%s", [apmtname,email,mobile,plot_no,address,landmark,city,pin,state,country,atype,rs,availability,Price,facilities,description,file,id,])
             mysql.connection.commit()
             cur.close()
             msg = ' Details have been successfully updated'
             return render_template("editapart.html",msg=msg,id=id,username=session['username'])
        else:
            msg = ' Please fill out the form !' 

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from apartmentdetail where A_ID=%s', [id,])
    data = cursor.fetchall()
    cursor.close()
    return render_template("editapart.html",datas=data,msg=msg,id=id,username=session['username'])

@app.route('/editroom/<string:id>', methods=['GET', 'POST'])
def editroom(id):
    msg = ''
    if request.method == 'POST':
        # fetch data
        details = request.form
        email = details['Email']
        mobile = details['Mobile']
        plot_no = details['Plot']
        address = details['Address']
        landmark = details['Landmark']
        city = details['City']
        pin = details['Pincode']
        state = details['State']
        country = details['Country']
        availability = details['status']
        Rent = details['Rent']
        facilities = details['Facilities']
        description = details['Description']
        file = request.files['file']
        extension = os.path.splitext(file.filename)
        f_name = str(uuid.uuid4()) + str(extension)
        app.config['UPLOAD_FOLDER'] = 'static/Uploads'
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
        if len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(facilities) > 0:
             cur = mysql.connection.cursor()
             cur.execute("UPDATE roomdetail SET Email =%s, Mobile =%s, Plot_no=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Availability=%s,Rent=%s,Facilities=%s,Descrption=%s,image=%s WHERE R_ID=%s", [email,mobile,plot_no,address,landmark,city,pin,state,country,availability,Rent,facilities,description,file,id,])
             mysql.connection.commit()
             cur.close()
             msg = ' Details have been successfully updated'
             return render_template("editroom.html",msg=msg,id=id,username=session['username'])
        else:
            msg = ' Please fill out the form !' 

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from roomdetail where R_ID=%s', [id,])
    data = cursor.fetchall()
    cursor.close()
    return render_template("editroom.html",datas=data,msg=msg,id=id,username=session['username'])

@app.route("/Buy_property/<string:id>",methods =['GET', 'POST'])
def Buy_property(id):
    if 'loggedin' in session:
        msg = ''
        if request.method == 'POST':
            A_ID = request.form['A_ID']
            Aname = request.form['Aname']
            Fullname = request.form['Fullname']
            Email = request.form['Email']
            Mobile = request.form['Mobile']
            Plot_no = request.form['Plot_no']
            Address = request.form['Address']
            Landmark = request.form['Landmark']
            City = request.form['City']
            Pincode = request.form['Pincode']
            State = request.form['State']
            Country = request.form['Country']
            if len(A_ID) > 0 and len(Aname) > 0 and len(Email) > 0 and len(Mobile) > 0 and len(Fullname) > 0 and len(
                    City) > 0 and len(Plot_no) > 0 and len(Address) > 0 and len(Landmark) > 0 and len(
                    Pincode) > 0 and len(State) > 0 and len(Country) > 0:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM Buy_propertyapt WHERE Email = % s', (Email,))
                account1 = cursor.fetchone()
                cursor.execute('SELECT * FROM Buy_propertyapt WHERE Mobile = % s', (Mobile,))
                account2 = cursor.fetchone()
                if not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
                    msg = 'Invalid email address !'
                elif len(Mobile) != 10:
                    msg = 'Enter 10 digit number !'
                else:
                    cursor.execute(
                        'INSERT INTO Buy_propertyapt VALUES (NULL, % s, % s, % s, % s, % s, % s, %s, %s, %s, %s, %s, %s)',
                        (A_ID, Aname, Fullname, Email, Mobile, Plot_no, Address, Landmark, City, Pincode, State,
                         Country))
                    mysql.connection.commit()
                    cursor.close()
                    msg = 'You have successfully registered !'
                    return render_template("index.html",username=session['username'], email1=session['email1'])
            else:
                msg = 'Please fill out the form !'
            #return render_template("Buy_property.html",msg=msg, username=session['username'])
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT Aname from apartmentdetail where A_ID=%s', [id,])
        data = cur.fetchall()
        cur.close()
        return render_template("Buy_property.html",datas=data,msg=msg,id=id,username=session['username'], email1=session['email1'])

    else:
        return redirect(url_for('login'))

@app.route("/details/")
def details():
    if 'loggedin' in session:
        return render_template('details.html', username='admin')
    return redirect(url_for('login'))

@app.route("/apartments/")
def apartments():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM apartmentdetail")
        if resultValue > 0:
            apartDetails = cur.fetchall()
            return render_template('apartments.html', apartDetails=apartDetails,username=session['username'])

@app.route("/rooms/")
def rooms():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM roomdetail")
        if resultValue > 0:
            roomDetails = cur.fetchall()
            return render_template('rooms.html', roomDetails=roomDetails,username=session['username'])

@app.route("/complaintlist/")
def complaintlist():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cursor = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM complaints")
        resultValue2 = cursor.execute("SELECT * FROM complaints2")
        if resultValue > 0 or resultValue2 > 0:
            complain1Details = cur.fetchall()
            complain2Details = cursor.fetchall()
            return render_template('complaintlist.html', complain1Details=complain1Details,complain2Details=complain2Details,username=session['username'])


    #return render_template('Buy_property.html', msg=msg,username=session['username'])


app.run(debug=True)
