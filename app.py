from flask import Flask, render_template


app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
   return render_template('home.html')



@app.route('/signup', methods=['GET'])
def signup():
   return render_template('signup.html')



@app.route('/login', methods=['GET'])
def login():
   return render_template('login.html')


@app.route('/c1', methods=['GET'])
def c1():
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

