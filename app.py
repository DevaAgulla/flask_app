from flask import Flask,render_template,request,flash

app = Flask(__name__)
app.secret_key = "manbearpig_deva"
@app.route("/hello")
def index():
    return render_template("index.html")

@app.route("/greet",methods=["POST","GET"])
def greet():
    session_id = request.form.get("name")
    flash(request.form.get("name"))
    print(session_id)
    return render_template("index.html")
   # print(session_id)

