from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)

# Create DB tables
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    # insert only if table is empty
    if Employee.query.first() is None:
        employee = Employee(
            name="Employee Name",
            email="Employee Email"
        )
        db.session.add(employee)
        db.session.commit()

    employees = Employee.query.all()
    return render_template("index.html", employees=employees)

@app.route('/about')
def about():
    return render_template("about2.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8069)
