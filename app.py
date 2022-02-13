from flask import Flask, request, session, redirect, url_for, render_template
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'

DB_HOST = "localhost"
DB_NAME = "s10"
DB_USER = "postgres"
DB_PASS = "papudirrtw"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

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
   return render_template('signup.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
   return render_template('login.html')


@app.route('/c1', methods=['GET'])
def c1():
   cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   if request.method == 'POST' and 'files' and 'productname1' and 'productmodel1' and 'productdescription1' and 'productprice1':
      files = request.files['files']
      productname1 = request.form['productname1']
      productmodel1 = request.form['productmodel1']
      productdescrition1 = request.form['productdescription1']
      productprice1 = request.form['productprice1']
      cursor.execute("INSERT INTO category_1 ((title), productname1, productmodel1, productdescription1, productprice1) VALUES (%s,%s,%s,%s,%s)", (files, productname1, productmodel1, productdescription1, productprice1))
      conn.commit()
   return render_template('c1.html')



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

