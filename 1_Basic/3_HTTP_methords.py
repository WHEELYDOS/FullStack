from flask import Flask  ,request

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route("/login", methords=['GET','POST'])
def login():
    if request.method=='POST':
        return do_the_login()
    else:
        return show_the_login_info()
    
def do_the_login():
    return f"login kaar na bc"

def show_the_login_info():
    return f"tera naam tere ko pata hoga na "


if __name__=="__main__":
    app.run(debug=True)