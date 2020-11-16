from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import os, uuid
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.secret_key = '66710c44ea2f24084dd73f9a'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'propertymanagement'

mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    op = ""
    if request.method == 'POST':
        loc = request.form['location']
        city = request.form['city']
        option = request.form['options']
        minprice = request.form['minprice']
        maxprice = request.form['maxprice']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        if option == "apartments":
            op = "a"
            if loc == "" and city == "" and minprice == "" and maxprice == "":
                cur.execute(
                    'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail')
                result = cur.fetchall()
            elif loc != "":
                if city == "" and minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s',
                        [loc])
                    result = cur.fetchall()
                elif city != "" and minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Aname,Username,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and City = %s',
                        ([loc], [city]))
                    result = cur.fetchall()
                elif city != "" and minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and City = %s and Price>=%s',
                        ([loc], [city], [minprice]))
                    result = cur.fetchall()
                elif city != "" and minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and City = %s and Price<=%s',
                        ([loc], [city], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and Price<=%s',
                        ([loc], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and Price<=%s',
                        ([loc], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and Price>=%s and Price<=%s',
                        ([loc], [minprice], [maxprice]))
                    result = cur.fetchall()
                elif city != "" and minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where State = % s and City=%s and Price>=%s and Price<=%s',
                        ([loc], [city], [minprice], [maxprice]))
                    result = cur.fetchall()
            elif city != "" and loc == "":
                if minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where City = % s',
                        [city])
                    result = cur.fetchall()
                elif minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where City = % s and Price<=%s',
                        ([city], [maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where City = % s and Price<=%s',
                        ([city], [maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where City = % s and Price>=%s and Price<=%s',
                        ([city], [minprice], [maxprice]))
                    result = cur.fetchall()
            elif city == "" and loc == "":
                if minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where Price<=%s',
                        ([maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where Price>=%s',
                        ([minprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT A_ID,Username,Aname,Email,Mobile,Plot_no,Address,Landmark,City,Pincode,State,Country,Price,Atype,RS,Availability,Facilities,Dscrption,image FROM apartmentdetail where Price>=%s and Price<=%s',
                        ([minprice], [maxprice]))
                    result = cur.fetchall()
        elif option == "rooms":
            op = "r"
            if loc == "" and city == "" and minprice == "" and maxprice == "":

                cur.execute(
                    'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail')
                result = cur.fetchall()
            elif loc != "":
                if city == "" and minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s',
                        [loc])
                    result = cur.fetchall()
                elif city != "" and minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and City = %s',
                        ([loc], [city]))
                    result = cur.fetchall()
                elif city != "" and minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and City = %s and Rent>=%s',
                        ([loc], [city], [minprice]))
                    result = cur.fetchall()
                elif city != "" and minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and City = %s and Rent<=%s',
                        ([loc], [city], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and Rent<=%s',
                        ([loc], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and Rent<=%s',
                        ([loc], [maxprice]))
                    result = cur.fetchall()
                elif city == "" and minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and Rent>=%s and Rent<=%s',
                        ([loc], [minprice], [maxprice]))
                    result = cur.fetchall()
                elif city != "" and minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where State = % s and City=%s and Rent>=%s and Rent<=%s',
                        ([loc], [city], [minprice], [maxprice]))
                    result = cur.fetchall()
            elif city != "" and loc == "":
                if minprice == "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where City = % s',
                        [city])
                    result = cur.fetchall()
                elif minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where City = % s and Rent<=%s',
                        ([city], [maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where City = % s and Rent<=%s',
                        ([city], [maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where City = % s and Rent>=%s and Price<=%s',
                        ([city], [minprice], [maxprice]))
                    result = cur.fetchall()
            elif city == "" and loc == "":
                if minprice == "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where Rent<=%s',
                        ([maxprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice == "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where Rent>=%s',
                        ([minprice]))
                    result = cur.fetchall()
                elif minprice != "" and maxprice != "":
                    cur.execute(
                        'SELECT R_ID,Username,Email,Mobile,Room_no,Address,Landmark,City,Pincode,State,Country,Availability,Facilities,Dscrption,image,Rent FROM roomdetail where Rent>=%s and Rent<=%s',
                        ([minprice], [maxprice]))

                    result = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        if result:
            if 'loggedin' in session:
                return render_template('index.html', detail=result, msg="Result for the search", op=op,
                                       username=session['username'])
            else:
                return render_template('index.html', detail=result, msg="Result for the search", op=op, username="")
        else:
            if 'loggedin' in session:
                return render_template('index.html', detail="No records found", username=session['username'])
            else:
                return render_template('index.html', detail="No records found", username="")
    else:
        if 'loggedin' in session:
            return render_template('index.html', username=session['username'])
        else:
            return render_template('index.html', username="")


@app.route("/about")
def about():
    if 'loggedin' in session:
        return render_template('about.html', username=session['username'])
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
            cursor.execute('SELECT * FROM accounts WHERE username = %s', (username, ))
            account = cursor.fetchone()
            mysql.connection.commit()
            cursor.close()
            if account and bcrypt.checkpw(password.encode('utf-8'), account['password'].encode('utf-8')):
                if username == 'admin' and password == 'admin':
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    session['email1'] = account['email']
                    session['mobile'] = account['mobile']
                    return redirect(url_for('dashboard'))
                else:
                    session['loggedin'] = True
                    session['id'] = account['id']
                    session['username'] = account['username']
                    session['email1'] = account['email']
                    session['mobile'] = account['mobile']
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
    session.pop('mobile', None)
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
                hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s,% s,% s,% s)',
                               (username, fullname, email, mobile, hashed, hashed,))
                mysql.connection.commit()
                cursor.close()
                msg = 'You have successfully registered !'
        else:
            msg = 'Please fill out the form !'

    return render_template('register.html', msg=msg)


@app.route("/dashboard/")
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username='admin', email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/userdashboard/")
def userdashboard():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cursor = mysql.connection.cursor()
        cursor1 = mysql.connection.cursor()
        cursor2 = mysql.connection.cursor()
        cursor3 = mysql.connection.cursor()
        cur1 = mysql.connection.cursor()
        resultValue = cur.execute("SELECT Aname,Fullname FROM Buy_propertyapt where Username=%s",
                                  [session['username'], ])
        result = cursor.execute("SELECT Aname,email,mobile FROM approved where Applicant=%s", [session['username'], ])
        result4 = cur1.execute("SELECT Room_no,email,mobile FROM approved2 where Applicant=%s", [session['username'], ])
        result1 = cursor1.execute("SELECT Room_no,Fullname FROM Buy_propertyroom where Username=%s",
                                  [session['username'], ])
        result2 = cursor2.execute(
            "SELECT Aname,Complaint,Flag FROM complaints where Flag=1 and A_ID in (select A_ID from apartmentdetail where Username=%s)",
            [session['username'], ])
        result3 = cursor3.execute(
            "SELECT Room_no,Complaint,Flag FROM complaints2 where Flag=1 and R_ID in (select R_ID from roomdetail where Username=%s)",
            [session['username'], ])
        if resultValue > 0 or result > 0 or result1 > 0 or result2 > 0 or result3 > 0 or result4 > 0:
            rental = cur.fetchall()
            outcome = cursor.fetchall()
            outcome2 = cur1.fetchall()
            rental2 = cursor1.fetchall()
            compapt = cursor2.fetchall()
            comproom = cursor3.fetchall()
            return render_template('userdashboard.html', rental=rental, outcome=outcome, outcome2=outcome2,rental2=rental2,
                                   compapt=compapt, comproom=comproom, username=session['username'],
                                   email1=session['email1'])
        else:
            return render_template('userdashboard.html', username=session['username'], email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/registeredusers/")
def registeredusers():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM accounts")
        if resultValue > 0:
            userDetails = cur.fetchall()
            return render_template('registeredusers.html', userDetails=userDetails, username=session['username'],
                                   email1=session['email1'])


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
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)
        allowed_extensions = {'.jpg', '.png', '.jpeg'}
        if extension[1] in allowed_extensions:
            f_name = str(uuid.uuid4()) + str(extension[1])
            app.config['UPLOAD_FOLDER'] = 'static/Uploads'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
            if len(apmtname) > 0 and len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(
                landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(
            atype) > 0 and len(facilities) > 0 and len(description) > 0:
             if len(mobile) != 10:
                msg = 'Enter 10 digit Mobile number !'
             elif len(pin) != 6:
                msg = 'Enter 6 digit Pincode !'
             elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
             elif not apmtname or not email or not mobile or not plot_no or not address or not landmark or not city or not pin or not state or not country or not atype or not facilities or not description or not file:
                msg = 'Please fill out the form !'
             else:
                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO apartmentdetail VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        apmtname, email, mobile, plot_no, address, landmark, city, pin, state, country, atype, rs,
                        availability,
                        Price, facilities, description, f_name, session['username']))
                mysql.connection.commit()
                cur.close()
                msg = 'Registration Successful! Thank You !'
            else:
              msg = 'Please fill out the form !'
        else:
            msg = 'Upload image in jpg/png/jpeg format only!'

    return render_template('Apmt_reg.html', username=session['username'], email1=session['email1'], msg=msg)


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
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)
        allowed_extensions = {'.jpg', '.png', '.jpeg'}
        if extension[1] in allowed_extensions:
            f_name = str(uuid.uuid4()) + str(extension[1])
            app.config['UPLOAD_FOLDER'] = 'static/Uploads'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))

            if len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(
                landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(
            availability) > 0 and len(rent) > 0 and len(facilities) > 0 and len(description) > 0:
              if len(mobile) != 10:
                msg = 'Enter 10 digit Mobile number !'
              elif len(pin) != 6:
                msg = 'Enter 6 digit Pincode !'
              elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                msg = 'Invalid email address !'
              elif not email or not mobile or not plot_no or not address or not landmark or not city or not pin or not state or not country or not availability or not rent or not facilities or not description or not file:
                msg = 'Please fill out the form !'
              else:
                cur = mysql.connection.cursor()
                cur.execute(
                    "INSERT INTO roomdetail VALUES(NULL, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
                    (email, mobile, plot_no, address, landmark, city, pin, state, country, availability, rent,
                     facilities, description, f_name, session['username']))
                mysql.connection.commit()
                cur.close()
                msg = 'Registration Successful! Thank You !'
            else:
              msg = 'Please fill out the form !'
        else:
            msg = 'Upload image in jpg/png/jpeg format only!'
    return render_template('roomreg.html', username=session['username'], email1=session['email1'], msg=msg)


@app.route('/complaints/<string:id>', methods=['GET', 'POST'])
def complaints(id):
    msg = ''
    if request.method == 'POST':
        data = request.form
        apmtname = data['name']
        complaint = data['complaint']
        if len(apmtname) > 0 and len(complaint) > 0:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO complaints VALUES(NULL, %s, %s, %s,0)", (id, apmtname, complaint))
            mysql.connection.commit()
            cur.close()
            msg = '   A complaint has been successfully registered'
        else:
            msg = '   Please fill out the form !'
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT Aname from apartmentdetail where A_ID=%s', [id, ])
    aptn = cur.fetchall()
    cur.close()
    if 'loggedin' in session:
        return render_template("complaints.html", msg=msg, datas=aptn, id=id, username=session['username'],
                               email1=session['email1'])
    else:
        return render_template("login.html")


@app.route('/complaints2/<string:id>', methods=['GET', 'POST'])
def complaints2(id):
    msg = ''
    if request.method == 'POST':
        data = request.form
        Room_no = data['Plot']
        complaint = data['complaint']
        if len(Room_no) > 0 and len(complaint) > 0:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO complaints2 VALUES(NULL, %s, %s, %s, 0)", [id, Room_no, complaint])

            mysql.connection.commit()
            cur.close()
            msg = '   A complaint has been successfully registered'
        else:
            msg = '   Please fill out the form !'
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute('SELECT Room_no from roomdetail where R_ID=%s', [id, ])
    no = cur.fetchall()
    cur.close()
    if 'loggedin' in session:
        return render_template("complaints2.html", msg=msg, datas=no, id=id, username=session['username'],
                               email1=session['email1'])
    else:
        return render_template("login.html")


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
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)
        allowed_extensions = {'.jpg', '.png', '.jpeg'}
        if extension[1] in allowed_extensions:
            f_name = str(uuid.uuid4()) + str(extension[1])
            app.config['UPLOAD_FOLDER'] = 'static/Uploads'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
            if len(apmtname) > 0 and len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(atype) > 0 and len(facilities) > 0:
                cur = mysql.connection.cursor()
                cur.execute("UPDATE apartmentdetail SET Aname=%s, Email =%s, Mobile =%s, Plot_no=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Atype=%s,RS=%s, Availability=%s,Price=%s,Facilities=%s,Dscrption=%s,image=%s WHERE A_ID=%s",[apmtname, email, mobile, plot_no, address, landmark, city, pin, state, country, atype, rs, availability, Price, facilities, description, f_name,id, ])
                mysql.connection.commit()
                cur.close()
                cursor1 = mysql.connection.cursor()
                cursor1.execute('SELECT * from apartmentdetail where A_ID=%s', [id,])
                data = cursor1.fetchall()
                cursor1.close()
                msg = ' Details have been successfully updated'
                return render_template("editapart.html",datas=data,msg=msg, id=id, username=session['username'],email1=session['email1'])
            else:
                msg = ' Please fill out the form !'

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from apartmentdetail where A_ID=%s', [id,])
    data = cursor.fetchall()
    cursor.close()
    return render_template("editapart.html",datas=data,msg=msg,id=id,username=session['username'], email1=session['email1'])


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
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)
        allowed_extensions = {'.jpg', '.png', '.jpeg'}
        if extension[1] in allowed_extensions:
            f_name = str(uuid.uuid4()) + str(extension[1])
            app.config['UPLOAD_FOLDER'] = 'static/Uploads'
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))
            if len(email) > 0 and len(mobile) > 0 and len(plot_no) > 0 and len(address) > 0 and len(
                    landmark) > 0 and len(city) > 0 and len(pin) > 0 and len(state) > 0 and len(country) > 0 and len(
                    facilities) > 0:
                cur = mysql.connection.cursor()
                cur.execute(
                    "UPDATE roomdetail SET Email =%s, Mobile =%s, Room_no=%s, Address=%s, Landmark=%s, City=%s, Pincode=%s, State=%s, Country=%s, Availability=%s,Rent=%s,Facilities=%s,Dscrption=%s,image=%s WHERE R_ID=%s",
                    [email, mobile, plot_no, address, landmark, city, pin, state, country, availability, Rent,
                     facilities, description, f_name, id, ])
                mysql.connection.commit()
                cur.close()
                cursor1 = mysql.connection.cursor()
                cursor1.execute('SELECT * from roomdetail where R_ID=%s', [id, ])
                data = cursor1.fetchall()
                cursor1.close()
                msg = ' Details have been successfully updated'
                return render_template("editroom.html",datas=data, msg=msg, id=id, username=session['username'],
                                       email1=session['email1'])
            else:
                msg = ' Please fill out the form !'

    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * from roomdetail where R_ID=%s', [id, ])
    data = cursor.fetchall()
    cursor.close()
    return render_template("editroom.html", datas=data, msg=msg, id=id, username=session['username'],
                           email1=session['email1'])


@app.route("/Buy_property/<string:id>", methods=['GET', 'POST'])
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
            Status = 'Not Approved'
            if len(A_ID) > 0 and len(Aname) > 0 and len(Email) > 0 and len(Mobile) > 0 and len(Fullname) > 0 and len(
                    City) > 0 and len(Plot_no) > 0 and len(Address) > 0 and len(Landmark) > 0 and len(
                Pincode) > 0 and len(State) > 0 and len(Country) > 0:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                if not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
                    msg = 'Invalid email address !'
                elif len(Mobile) != 10:
                    msg = 'Enter 10 digit number !'
                else:
                    cursor1 = mysql.connection.cursor()
                    cursor1.execute('SELECT Username from apartmentdetail where A_ID=%s', [A_ID, ])
                    user = cursor1.fetchall()
                    cursor1.close()
                    cursor.execute(
                        'INSERT INTO Buy_propertyapt VALUES (NULL, % s, % s, % s, % s, % s, % s, %s, %s, %s, %s, %s, %s, %s,%s,%s)',
                        (A_ID, Aname, Fullname, Email, Mobile, Plot_no, Address, Landmark, City, Pincode, State,
                         Country, user[0], session['username'],Status))
                    mysql.connection.commit()
                    cursor.close()
                    return render_template("index.html", username=session['username'], email1=session['email1'])
            else:
                msg = 'Please fill out the form !'
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT Aname from apartmentdetail where A_ID=%s', [id, ])
        data = cur.fetchall()
        cur.close()
        return render_template("Buy_property.html", datas=data, msg=msg, id=id, username=session['username'],
                               email1=session['email1'])

    else:
        return redirect(url_for('login'))


@app.route("/Buy_propertyroom/<string:id>", methods=['GET', 'POST'])
def Buy_propertyroom(id):
    if 'loggedin' in session:
        msg = ''
        if request.method == 'POST':
            R_ID = request.form['R_ID']
            Room_no = request.form['Room_no']
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
            Status = 'Not Approved'
            if len(R_ID) > 0 and len(Room_no) > 0 and len(Email) > 0 and len(Mobile) > 0 and len(Fullname) > 0 and len(
                    City) > 0 and len(Plot_no) > 0 and len(Address) > 0 and len(Landmark) > 0 and len(
                Pincode) > 0 and len(State) > 0 and len(Country) > 0:
                cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
                cursor.execute('SELECT * FROM Buy_propertyroom WHERE Email = % s', (Email,))
                account1 = cursor.fetchone()
                cursor.execute('SELECT * FROM Buy_propertyroom WHERE Mobile = % s', (Mobile,))
                account2 = cursor.fetchone()
                if not re.match(r'[^@]+@[^@]+\.[^@]+', Email):
                    msg = 'Invalid email address !'
                elif len(Mobile) != 10:
                    msg = 'Enter 10 digit number !'
                else:
                    cursor1 = mysql.connection.cursor()
                    cursor1.execute('SELECT Username from roomdetail where R_ID=%s', [R_ID, ])
                    user = cursor1.fetchall()
                    cursor1.close()
                    cursor.execute(
                        'INSERT INTO Buy_propertyroom VALUES (NULL, % s, % s, % s, % s, % s, % s, %s, %s, %s, %s, %s, %s, %s,%s,%s)',
                        (R_ID, Room_no, Fullname, Email, Mobile, Plot_no, Address, Landmark, City, Pincode, State,
                         Country, user[0], session['username'],Status))
                    mysql.connection.commit()
                    cursor.close()
                    msg = 'You have successfully registered !'
                    return render_template("index.html", username=session['username'], email1=session['email1'])
            else:
                msg = 'Please fill out the form !'
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('SELECT Room_no from roomdetail where R_ID=%s', [id, ])
        data = cur.fetchall()
        cur.close()
        return render_template("Buy_propertyroom.html", datas=data, msg=msg, id=id, username=session['username'],
                               email1=session['email1'])

    else:
        return redirect(url_for('login'))


@app.route("/details/")
def details():
    if 'loggedin' in session:
        return render_template('details.html', username='admin', email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/apartments/")
def apartments():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM apartmentdetail")
        if resultValue > 0:
            apartDetails = cur.fetchall()
            return render_template('apartments.html', msg=msg, apartDetails=apartDetails, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Apartments for rent as of now'
            return render_template('apartments.html', msg=msg, username=session['username'], email1=session['email1'])
        cur.close()


@app.route("/delete1/<string:id>")
def delete1(id):
    msg = ''
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM apartmentdetail where A_ID=%s", [id, ])
    mysql.connection.commit()
    cursor.close()
    cur1 = mysql.connection.cursor()
    if session['username'] != "admin":
        resultValue = cur1.execute("SELECT * FROM apartmentdetail where Username=%s", (session['username'],))
        apartDetails = cur1.fetchall()
        if resultValue > 0:
            return render_template('ownerapartments.html', msg=msg, apartDetails=apartDetails,
                                   username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Apartments for rent as of now'
            return render_template('ownerapartments.html', msg=msg, username=session['username'],
                                   email1=session['email1'])
    else:
        resultValue = cur1.execute("SELECT * FROM apartmentdetail ")
        apartDetails = cur1.fetchall()
        if resultValue > 0:
            return render_template('apartments.html', msg=msg, apartDetails=apartDetails, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Apartments for rent as of now'
            return render_template('apartments.html', msg=msg, username=session['username'], email1=session['email1'])
    cur1.close()


@app.route("/delete2/<string:id>")
def delete2(id):
    msg = ''
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM roomdetail where R_ID=%s", [id, ])
    mysql.connection.commit()
    cursor.close()
    cur1 = mysql.connection.cursor()
    if session['username'] != "admin":
        resultValue = cur1.execute("SELECT * FROM roomdetail where Username=%s", (session['username'],))
        roomDetails = cur1.fetchall()
        if resultValue > 0:
            return render_template('ownerrooms.html', msg=msg, roomDetails=roomDetails,
                                   username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Rooms for rent as of now'
            return render_template('ownerrooms.html', msg=msg, username=session['username'],
                                   email1=session['email1'])
    else:
        resultValue = cur1.execute("SELECT * FROM roomdetail ")
        roomDetails = cur1.fetchall()
        if resultValue > 0:
            return render_template('rooms.html', msg=msg, roomDetails=roomDetails, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Rooms for rent as of now'
            return render_template('rooms.html', msg=msg, username=session['username'], email1=session['email1'])
    cur1.close()


@app.route("/rooms/")
def rooms():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM roomdetail")
        if resultValue > 0:
            roomDetails = cur.fetchall()
            return render_template('rooms.html', msg=msg, roomDetails=roomDetails, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no Rooms for rent as of now'
            return render_template('rooms.html', msg=msg, username=session['username'], email1=session['email1'])


@app.route("/approval/")
def approval():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM Buy_propertyapt where Username=%s", [session['username'], ])
        if resultValue > 0:
            apply = cur.fetchall()
            cursor = mysql.connection.cursor()
            result = cursor.execute("SELECT Aname FROM Buy_propertyapt GROUP BY Aname")
            apply2 = cursor.fetchall()
            return render_template('approval.html', msg=msg, apply2=apply2, apply=apply, username=session['username'],
                                   email1=session['email1'])
            cursor.close()
        else:
            msg = 'There are no applicants for any of your registered apartments'
            return render_template('approval.html', msg=msg, username=session['username'], email1=session['email1'])
        cur.close()

@app.route("/approval2/")
def approval2():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM Buy_propertyroom where Username=%s", [session['username'], ])
        if resultValue > 0:
            apply = cur.fetchall()
            cursor = mysql.connection.cursor()
            result = cursor.execute("SELECT Room_no FROM Buy_propertyroom GROUP BY Room_no")
            apply2 = cursor.fetchall()
            return render_template('approval2.html', msg=msg, apply2=apply2, apply=apply, username=session['username'],
                                   email1=session['email1'])
            cursor.close()
        else:
            msg = 'There are no applicants for any of your registered apartments'
            return render_template('approval2.html', msg=msg, username=session['username'], email1=session['email1'])
        cur.close()

@app.route("/approve/<string:id>/<Aname>/<Fullname>")
def approve(id, Aname, Fullname):
    msg = ''
    Status = 'Approved'
    cur1 = mysql.connection.cursor()
    cur1.execute("INSERT INTO approved VALUES (NULL, %s, %s,(select Email from apartmentdetail where Username=%s and Aname=%s),(select Mobile from apartmentdetail where Username=%s and Aname=%s))",[Aname, Fullname,session['username'],Aname, session['username'],Aname, ])
    mysql.connection.commit()
    cur1.close()
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Buy_propertyapt SET Status=%s where bapt_id=%s", [Status,id, ])
    mysql.connection.commit()
    cursor.close()
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Buy_propertyapt where Username=%s", [session['username'], ])
    if resultValue > 0:
        apply = cur.fetchall()
        cursor1 = mysql.connection.cursor()
        result = cursor1.execute("SELECT Aname FROM Buy_propertyapt GROUP BY Aname")
        apply2 = cursor1.fetchall()
        return render_template('approval.html', msg=msg, apply2=apply2, apply=apply, username=session['username'], email1=session['email1'])
        cursor1.close()
    else:
        msg = 'There are no applicants for any of your registered apartments'
        return render_template('approval.html', msg=msg, username=session['username'], email1=session['email1'])
    cur.close()

@app.route("/approve2/<string:id>/<Room_no>/<Fullname>")
def approve2(id, Room_no, Fullname):
    msg = ''
    Status = 'Approved'
    cur1 = mysql.connection.cursor()
    cur1.execute("INSERT INTO approved2 VALUES (NULL, %s, %s,(select Email from roomdetail where Username=%s and Room_no=%s),(select Mobile from roomdetail where Username=%s and Room_no=%s))",[Room_no, Fullname,session['username'],Room_no,session['username'],Room_no, ])
    mysql.connection.commit()
    cur1.close()
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE Buy_propertyroom SET Status=%s where bapt_id=%s", [Status,id, ])
    mysql.connection.commit()
    cursor.close()
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Buy_propertyroom where Username=%s", [session['username'], ])
    if resultValue > 0:
        apply = cur.fetchall()
        cursor1 = mysql.connection.cursor()
        result = cursor1.execute("SELECT Room_no FROM Buy_propertyroom GROUP BY Room_no")
        apply2 = cursor1.fetchall()
        return render_template('approval2.html', msg=msg, apply2=apply2, apply=apply, username=session['username'], email1=session['email1'])
        cursor1.close()
    else:
        msg = 'There are no applicants for any of your registered apartments'
        return render_template('approval2.html', msg=msg, username=session['username'], email1=session['email1'])
    cur.close()

@app.route("/reject/<string:id>/")
def reject(id):
    msg = ''
    Status = 'Rejected'
    cur1 = mysql.connection.cursor()
    cur1.execute("DELETE FROM Buy_propertyapt where bapt_id=%s", [id, ])
    mysql.connection.commit()
    cur1.close()
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Buy_propertyapt where Username=%s", [session['username'], ])
    if resultValue > 0:
        apply = cur.fetchall()
        cursor1 = mysql.connection.cursor()
        result = cursor1.execute("SELECT Aname FROM Buy_propertyapt GROUP BY Aname")
        apply2 = cursor1.fetchall()
        return render_template('approval.html', msg=msg, apply2=apply2, apply=apply, username=session['username'], email1=session['email1'])
        cursor1.close()
    else:
        msg = 'There are no applicants for any of your registered apartments'
        return render_template('approval.html', msg=msg, username=session['username'], email1=session['email1'])
    cur.close()

@app.route("/reject2/<string:id>/")
def reject2(id):
    msg = ''
    Status = 'Rejected'
    cur1 = mysql.connection.cursor()
    cur1.execute("DELETE FROM Buy_propertyroom where bapt_id=%s", [id, ])
    mysql.connection.commit()
    cur1.close()
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Buy_propertyroom where Username=%s", [session['username'], ])
    if resultValue > 0:
        apply = cur.fetchall()
        cursor1 = mysql.connection.cursor()
        result = cursor1.execute("SELECT Room_no FROM Buy_propertyroom GROUP BY Room_no")
        apply2 = cursor1.fetchall()
        return render_template('approval2.html', msg=msg, apply2=apply2, apply=apply, username=session['username'], email1=session['email1'])
        cursor1.close()
    else:
        msg = 'There are no applicants for any of your registered apartments'
        return render_template('approval2.html', msg=msg, username=session['username'], email1=session['email1'])
    cur.close()


@app.route("/complaintlist/")
def complaintlist():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        cursor = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM complaints")
        resultValue2 = cursor.execute("SELECT * FROM complaints2")
        if resultValue > 0 or resultValue2 > 0:
            complain1Details = cur.fetchall()
            complain2Details = cursor.fetchall()
            return render_template('complaintlist.html', msg=msg, complain1Details=complain1Details,
                                   complain2Details=complain2Details, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'There are no complaints as of now'
            return render_template('complaintlist.html', msg=msg, username=session['username'],
                                   email1=session['email1'])



@app.route('/warn/<string:id>/<string:cid>', methods=['GET', 'POST'])
def warn(id, cid):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE complaints SET Flag=1 WHERE A_ID=%s and C_ID=%s", [id, cid])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('complaintlist'))


@app.route('/warn1/<string:id>/<string:cid>', methods=['GET', 'POST'])
def warn1(id, cid):
    cur = mysql.connection.cursor()
    cur.execute("UPDATE complaints2 SET Flag=1 WHERE R_ID=%s and C_ID=%s", [id, cid, ])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('complaintlist'))


@app.route("/ownerpropdetails/")
def ownerpropdetails():
    if 'loggedin' in session:
        return render_template('ownerpropdetails.html', username=session['username'], email1=session['email1'])
    return redirect(url_for('login'))


@app.route("/ownerapartments/")
def ownerapartments():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM apartmentdetail where Username=%s", (session['username'],))
        if resultValue > 0:
            apartDetails = cur.fetchall()
            return render_template('ownerapartments.html', msg=msg, apartDetails=apartDetails,
                                   username=session['username'], email1=session['email1'])
        else:
            msg = 'No Apartments registered by you as of now'
            return render_template('ownerapartments.html', msg=msg, username=session['username'],
                                   email1=session['email1'])


@app.route("/ownerrooms/")
def ownerrooms():
    msg = ''
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM roomdetail where Username=%s", (session['username'],))
        if resultValue > 0:
            roomDetails = cur.fetchall()
            return render_template('ownerrooms.html', msg=msg, roomDetails=roomDetails, username=session['username'],
                                   email1=session['email1'])
        else:
            msg = 'No Room Registered by you as of now'
            return render_template('ownerrooms.html', msg=msg, username=session['username'], email1=session['email1'])


app.run(debug=True)
