import flask
from flask import jsonify, request

from . import db_session
from .jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                                    'is_finished', 'team_leader_id')) for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).get(job_id)
    if not jobs:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'jobs': jobs.to_dict(only=('team_leader', 'job', 'work_size', 'collaborators', 'start_date', 'end_date',
                                       'is_finished', 'team_leader_id'))
        }
    )


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    db_sess = db_session.create_session()
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['team_leader', 'job', 'work_size', 'collaborators', 'is_finished', 'team_leader_id']):
        return jsonify({'error': 'Bad request'})
    # тут не уверен, сообщение в тг от 13.03.2023 23:37
    elif db_sess.query(Jobs).get(request.json['team_leader_id']):
        return jsonify({"error": "Id already exists"})
    jobs = Jobs(
        team_leader=request.json['team_leader'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished'],
        team_leader_id=request.json['team_leader_id'],
    )
    db_sess.add(jobs)
    db_sess.commit()
    return jsonify({'success': 'OK'})
