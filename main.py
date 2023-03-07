import datetime

from flask import Flask, render_template
from data import db_session
from data.db_session import create_session, global_init
from data.users import User
from data.news import News
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'itsdenisska2007supertop4ik'


@app.route("/")
def index():
    global_init("db/blogs.sqlite")
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", jobs=jobs, length=len(list(jobs)))


if __name__ == '__main__':
    app.run(debug=True, port=5002)
