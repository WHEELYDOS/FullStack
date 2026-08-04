import os
from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "supersecretkey"

db = SQLAlchemy(app)


class Employee(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        if not name or not email:
            flash("All fields are required", "danger")
            return redirect('/')

        employee = Employee(name=name, email=email)
        db.session.add(employee)
        db.session.commit()
        flash("Form submission successful", "success")
        return redirect('/')

    allemployee = Employee.query.all()
    return render_template("index.html", employees=allemployee)


@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employee.query.filter_by(sno=sno).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect("/")


@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update(sno):
    employee = Employee.query.filter_by(sno=sno).first()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()

        if employee:
            employee.name = name
            employee.email = email
            db.session.commit()

        return redirect("/")

    return render_template("update.html", employee=employee)


@app.route('/about')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render default is 10000
    app.run(host="0.0.0.0", port=port)