import datetime

from flask import Flask, render_template, make_response, jsonify
from flask_restful import Api

from data import db_session, jobs_api, users_resource
from data.db_session import create_session, global_init
from data.users import User
from data.news import News
from data.jobs import Jobs

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'itsdenisska2007supertop4ik'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs)
    return render_template("index.html", jobs=jobs, length=len(list(jobs)))


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(400)
def bad_request(_):
    return make_response(jsonify({'error': 'Bad Request'}), 400)


if __name__ == '__main__':
    global_init("db/blogs.sqlite")
    app.register_blueprint(jobs_api.blueprint)
    api.add_resource(users_resource.UsersListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/user/<int:user_id>')
    app.run(debug=True, port=5003)
