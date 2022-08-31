from flask import Flask,render_template,request,flash

app = Flask(__name__)

@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/feed",methods=["POST","GET"])
def feed():
    session_id = request.form['name']
    flash("ur"+"sessid"+session_id)
