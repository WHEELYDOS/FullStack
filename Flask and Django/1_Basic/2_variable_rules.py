from flask import Flask , request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hello World"

@app.route("/usr/<username>")
def user_info(username):
    return f"User {escape(username)}"

@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Your post id is {escape(post_id)}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

with app.test_request_context():
    print(url_for('hello'))
    print(url_for('hello',next ='/'))
    print(url_for('user_info', username = "harsh"))
    print(url_for('post',post_id=6969))
    print(url_for('show_subpath',subpath="harsh/sahu"))



if __name__ == "__main__":
    app.run (debug=True)