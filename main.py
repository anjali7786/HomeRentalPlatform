from flask import Flask,render_template,request,redirect,url_for,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re


app = Flask(__name__)

app.secret_key = '66710c44ea2f24084dd73f9a'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'propertymanagement'
mysql = MySQL(app)


@app.route("/login/", methods=['GET','POST'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if len(username)>0 and len(password)>0:
         cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
         cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))
         account = cursor.fetchone()
         mysql.connection.commit()
         cursor.close()
         if account:
             if username=='admin' and password=='admin':
              session['loggedin'] = True
              session['id'] = account['id']
              session['username'] = account['username']
              return redirect(url_for('dashboard'))
             else:
              msg= 'Logged in successfully!'
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
   return redirect(url_for('login'))


@app.route("/register/", methods=['GET','POST'])
def register():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        fullname = request.form['fullname']
        password = request.form['password']
        email = request.form['email']
        mobile = request.form['mobile']
        cpassword = request.form['cpassword']
        if len(username)>0 and len(password)>0 and len(email)>0 and len(mobile)>0 and len(fullname)>0 and len(cpassword)>0:
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
            msg= 'Account already exists with this email !'
         elif account2:
            msg= 'Account already exists with this mobile number !'
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
            cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s,% s,% s,% s)', (username, fullname, email, mobile, password, cpassword,))
            mysql.connection.commit()
            cursor.close()
            msg = 'You have successfully registered !'
        else:
           msg = 'Please fill out the form !'

    return render_template('register.html', msg=msg)

@app.route("/dashboard/")
def dashboard():
    if 'loggedin' in session:
        return render_template('dashboard.html', username=session['username'])
    return redirect(url_for('login'))

@app.route("/registeredusers/")
def registeredusers():
    if 'loggedin' in session:
        cur = mysql.connection.cursor()
        resultValue = cur.execute("SELECT * FROM accounts")
        if resultValue > 0:
            userDetails = cur.fetchall()
            return render_template('registeredusers.html', userDetails=userDetails,username=session['username'])


app.run(debug=True)