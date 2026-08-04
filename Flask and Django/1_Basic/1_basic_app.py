from flask import Flask,request
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def hello_world():
    name = request.args.get("name","Harsh")
    return f"<< Hello {escape(name)} this is your Home Page >> "


@app.route("/test")
def test():
    return f"<< This is your testing page >>"

if __name__ == "__main__":
    app.run (debug=True)