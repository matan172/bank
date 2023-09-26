from flask import Flask,session,redirect,render_template,request
import db

app = Flask("__main__")
app.secret_key = 'super secret key'



@app.route('/')
def index():
    if session: 
        user = db.pulluser(session["id"])
    else: user = False
    return render_template("index.html", session = session ,user = user)

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        userid = db.loginChecker(username=username,password=password)
        if userid: 
            session["id"] = userid
            return redirect("/")
    return "no username or password wrong"

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        repassword = request.form.get("repassword")
        if not (password == repassword):
            return "passwords dont match"
        db.adduser(username,password)
        return redirect ("/")
    return "no"

@app.route('/addbalace',methods=["POST","GET"])
def addbalance():
    balance = request.form.get('balance')
    try: balance = int(balance)
    except: return "please pass numbers in balance"
    db.addbalance(session["id"],balance)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)