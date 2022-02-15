from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
UPLOAD_FOLDER1 = 'static/upload1'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'
app.config['UPLOAD_FOLDER1'] = UPLOAD_FOLDER1

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
      cursor.execute("INSERT INTO users (firstname,lastname,nic,phonenumber, email, password,confirmPassword ) VALUES (%s,%s,%s,%s,%s,%s,%s)", (firstName,lastName, nic,phonenumber, email,password,confirmPassword))
      conn.commit()
      return redirect(url_for('/'))
   return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
   cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
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
            if password(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id']
                session['email'] = account['email']
                # Redirect to home page
                return redirect(url_for('/'))
               
   return render_template('login.html')


@app.route('/c1', methods=['GET','POST'])
def c1():
   mycursor.execute("SELECT * FROM category_1")
   data = mycursor.fetchall()
   print(data)
   return render_template('c1.html', data=data)

@app.route('/upload', methods=['GET','POST'])
def upload():
   cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   if request.method == 'POST':
      filenames ='';
      files = request.files.to_dict()
      print(files)
      
      files = request.files.getlist("files[]")
      for file in files:
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER1'], filename))
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


@app.route('/c2', methods=['GET'])
def c2():
   return render_template('c2.html')



@app.route('/c3', methods=['GET'])
def c3():
   return render_template('c3.html')



@app.route('/c4', methods=['GET'])
def c4():
   return render_template('c4.html')



if __name__ == '__main__':
   app.run(debug=True, port=5000)

