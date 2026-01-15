from flask import Flask , request
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

if __name__ == "__main__":
    app.run (debug=True)