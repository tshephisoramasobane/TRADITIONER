from flask import Flask,render_template,sessions,request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=["GET,POST"])
def submit():
    name = request.get("name")



















