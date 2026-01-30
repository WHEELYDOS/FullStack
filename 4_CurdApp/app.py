from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#config of db
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False


db = SQLAlchemy(app)
app.app_context().push()
class Employee(db.Model):
    sno=db.Column(db.Integer,primary_key=True)
    name = db.column(db.String(200),nullable=False)
    email  = db.column(db.String(500),nullable= False)



@app.route("/")
def home():
    return render_template("index.html")
    #return "this is your default landing page"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8069)