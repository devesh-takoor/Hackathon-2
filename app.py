from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER = 'static/'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


DB_HOST = "localhost"
DB_NAME = "s10"
DB_USER = "postgres"
DB_PASS = "papudirrtw"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
mycursor =conn.cursor()

@app.route('/', methods=['GET'])
def home():


    return render_template('home.html')



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST' and 'firstName' and 'lastName' and 'nic' and 'phonenumber' and 'email' and 'password' and 'confirmPassword':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        nic = request.form['nic']
        phonenumber = request.form['phonenumber']
        email = request.form['email']
        password = request.form['password'] 
        confirmPassword = request.form['confirmPassword']

        _hashed_password = generate_password_hash(password)

        #Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE nic = %s', (nic,))
        account = cursor.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', nic):
            flash('Username must contain only characters and numbers!')
        elif not nic or not password or not email:
            flash('Please fill out the form!')
        else:
            cursor.execute("INSERT INTO users (firstname,lastname,nic,phonenumber, email, password,confirmPassword ) VALUES (%s,%s,%s,%s,%s,%s,%s)", (firstName,lastName, nic,phonenumber, email,password,confirmPassword))
            conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        print(password)
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
        # Fetch one record and return result
        account = cursor.fetchone()

        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['email'] = account['username']
                # Redirect to home page
                return redirect(url_for('/'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect email/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect email/password')
    return render_template('login.html')



@app.route('/c1', methods=['GET','POST'])
def c1():
    mycursor.execute("SELECT * FROM category_1")
    data = mycursor.fetchall()
    print(data)
    return render_template('c1.html', data=data)

@app.route('/upload', methods=['GET','POST'])
def upload1():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        filenames ='';
        files = request.files.to_dict()
        print(files)

        files = request.files.getlist("files[]")
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames += filename + ';'
        filenames=filenames[:-1]
        productname1 = request.form['productname1']
        productmodel1 = request.form['productmodel1']
        productdescription1 = request.form['productdescription1']
        productprice1 = request.form['productprice1']
        cursor.execute("INSERT INTO category_1 (productname1, productmodel1, productdescription1, productprice1,filenames) VALUES (%s,%s,%s,%s,%s)", (productname1, productmodel1, productdescription1, productprice1,filenames))

        conn.commit()
        mycursor.execute("SELECT * FROM category_1")
        data = mycursor.fetchall()
    return redirect(url_for('c1'))


@app.route('/c2', methods=['GET','POST'])
def c2():
    mycursor.execute("SELECT * FROM category_2")
    data = mycursor.fetchall()
    print(data)
    return render_template('c2.html', data=data)

@app.route('/upload2', methods=['GET','POST'])
def upload2():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        filenames ='';
        files = request.files.to_dict()
        print(files)

        files = request.files.getlist("files[]")
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames += filename + ';'
            filenames=filenames[:-1]
        productname2 = request.form['productname2']
        productmodel2 = request.form['productmodel2']
        productdescription2 = request.form['productdescription2']
        productprice2 = request.form['productprice2']
        cursor.execute("INSERT INTO category_2 (productname2, productmodel2, productdescription2, productprice2,filenames) VALUES (%s,%s,%s,%s,%s)", (productname2, productmodel2, productdescription2, productprice2,filenames))

        conn.commit()
        mycursor.execute("SELECT * FROM category_2")
        data = mycursor.fetchall()
    return redirect(url_for('c2'))



@app.route('/c3', methods=['GET','POST'])
def c3():
    mycursor.execute("SELECT * FROM category_3")
    data = mycursor.fetchall()
    print(data)
    return render_template('c3.html', data=data)

@app.route('/upload3', methods=['GET','POST'])
def upload3():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        filenames ='';
        files = request.files.to_dict()
        print(files)

        files = request.files.getlist("files[]")
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames += filename + ';'
        filenames=filenames[:-1]
        productname3 = request.form['productname3']
        productmodel3 = request.form['productmodel3']
        productdescription3 = request.form['productdescription3']
        productprice3 = request.form['productprice3']
        cursor.execute("INSERT INTO category_3 (productname3, productmodel3, productdescription3, productprice3,filenames) VALUES (%s,%s,%s,%s,%s)", (productname3, productmodel3, productdescription3, productprice3,filenames))

        conn.commit()
        mycursor.execute("SELECT * FROM category_3")
        data = mycursor.fetchall()
    return redirect(url_for('c3'))



@app.route('/c4', methods=['GET','POST'])
def c4():
    mycursor.execute("SELECT * FROM category_4")
    data = mycursor.fetchall()
    print(data)
    return render_template('c4.html', data=data)

@app.route('/upload4', methods=['GET','POST'])
def upload4():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if request.method == 'POST':
        filenames ='';
        files = request.files.to_dict()
        print(files)

        files = request.files.getlist("files[]")
        for file in files:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames += filename + ';'
        filenames=filenames[:-1]
        productname4 = request.form['productname4']
        productmodel4 = request.form['productmodel4']
        productdescription4 = request.form['productdescription4']
        productprice4 = request.form['productprice4']
        cursor.execute("INSERT INTO category_4 (productname4, productmodel4, productdescription4, productprice4,filenames) VALUES (%s,%s,%s,%s,%s)", (productname4, productmodel4, productdescription4, productprice4,filenames))

        conn.commit()
        mycursor.execute("SELECT * FROM category_4")
        data = mycursor.fetchall()
    return redirect(url_for('c4'))



if __name__ == '__main__':
   app.run(debug=True, port=5000)
