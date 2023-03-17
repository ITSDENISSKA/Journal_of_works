import datetime

from requests import get, post

print(post('http://127.0.0.1:5003/api/jobs', json={
    'team_leader': 1,
    'job': 'послушать гс в тг',
    'work_size': 15,
    'collaborators': '2, 5',
    'is_finished': False,
    'team_leader_id': 2, }).json())
